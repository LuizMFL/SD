import pika
import uuid
import ast
from threading import Thread, Lock
from time import sleep

class RpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.internal_lock = Lock()
        self.corr_id = str(uuid.uuid4())
        thread = Thread(target=self.call)
        thread2 = Thread(target=self.process_data)
        thread.setDaemon(True)
        thread2.setDaemon(True)
        thread.start()
        thread2.start()
        thread.join()
        
        
    def process_data(self):
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
        while True:
            with self.internal_lock:
                self.connection.process_data_events()
                sleep(0.1)
            
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            body = body.decode('utf-8')
            body = dict(ast.literal_eval(body))
            print('[.] Got id({}): {} = {}'.format(body['uuid'], body['input'], body['output']))

    def call(self):
        operations = [  'sum(10, 20)', 
                        'sub(10, 58)',
                        'mult(34, -3)',
                        'div(40, 2)',
                        'loge(100)',
                        'log10(100)',
                        'exp(5, 4)',
                        'sin(3.14)',
                        'cos(3.14)',
                        'sqrt(64)'
        ]
        for x in operations:
            body = {
                'input': str(x),
                'output': '',
                'uuid': str(self.corr_id)
            }
            print('[x] Request id({}): {}...'.format(body['uuid'], body['input']))
            with self.internal_lock:
                self.channel.basic_publish(
                    exchange='Calculadora',
                    routing_key='rpc_queue2',
                    properties=pika.BasicProperties(
                        reply_to=self.callback_queue,
                        correlation_id=self.corr_id,
                    ),
                    body=str(body))


if __name__ == '__main__':
    RpcClient()
