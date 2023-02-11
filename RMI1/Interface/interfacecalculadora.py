import abc

class InterfaceCalculadora(abc.ABCMeta):
    @abc.abstractmethod
    def somar(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def subtrair(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def multiplicar(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def dividir(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def loge(self, x:float):
        raise NotImplementedError
    @abc.abstractmethod
    def log10(self, x:float):
        raise NotImplementedError
    @abc.abstractmethod
    def exp(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def sin(self, x:float):
        raise NotImplementedError
    @abc.abstractmethod
    def cos(self, x:float):
        raise NotImplementedError
    @abc.abstractmethod
    def sqrt(self, x:float):
        raise NotImplementedError
