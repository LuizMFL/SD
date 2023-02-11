from calculadora import Calculadora
import Pyro4


class Server:
    def __init__(self) -> None:
        daemon = Pyro4.Daemon.serveSimple({Calculadora: 'calc', }, port= 5500, ns=False, verbose=True)
        daemon.requestLoop()
if __name__ == '__main__':
    Server()