import pika
from calculadora import Calculadora
import ast

class Server:
    def __init__(self) -> None:
        self.calculadora = Calculadora()
        self.operacoes = {
            'sum': self.calculadora.sum,
            'sub': self.calculadora.sub,
            'mult': self.calculadora.mult,
            'div': self.calculadora.div,
            'exp': self.calculadora.exp,
            'loge': self.calculadora.loge,
            'log10': self.calculadora.log10,
            'sin': self.calculadora.sin,
            'cos': self.calculadora.cos,
            'sqrt': self.calculadora.sqrt
        }
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='Calculadora', exchange_type='direct')
        self.channel.queue_declare(queue='rpc_queue2', exclusive=True)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.queue_bind(exchange='Calculadora', queue='rpc_queue2')
        self.channel.basic_consume(queue='rpc_queue2', on_message_callback=self.on_request)
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        body = body.decode('utf-8')
        body = dict(ast.literal_eval(body))
        escolha = body["input"]
        constants = []
        for x in range(3,len(escolha)):
            if escolha[x] == '(':
                op = escolha[:x]
                resto = escolha[x:]
                resto = resto.replace('(', '').replace(')', '')
                if resto.count(','):
                    resto = resto.split(',')
                    constants.append(float(resto[0]))
                    constants.append(float(resto[1]))
                else:
                    constants = float(resto)
                break
        response = None
        if isinstance(constants, list):
            response = self.operacoes[op](constants[0], constants[1])
        else:
            response = self.operacoes[op](constants)
        body['output'] = str(response)
        print('[.] {}'.format(body['input']))
        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = props.correlation_id),
                        body=str(body))
        ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    Server()