import abc

class InterfaceCalculadora(abc.ABCMeta):
    @abc.abstractmethod
    def sum(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def sub(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def mult(self, x:float, y:float):
        raise NotImplementedError
    @abc.abstractmethod
    def div(self, x:float, y:float):
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
