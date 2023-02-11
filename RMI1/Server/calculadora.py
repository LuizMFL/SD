
import math

import Pyro4

@Pyro4.expose
class Calculadora:
    def sum(self, x: float, y: float):
        return x + y
    def sub(self, x: float, y: float):
        return x - y
    def mult(self, x: float, y: float):
        return x * y
    def div(self, x: float, y: float):
        return x / y
    def loge(self, x: float):
        return math.log(x)
    def log10(self, x: float):
        return math.log10(x)
    def exp(self, x: float, y: float):
        return x ** y
    def sin(self, x: float):
        return math.sin(x)
    def cos(self, x: float):
        return math.cos(x)
    def sqrt(self, x: float):
        return math.sqrt(x)
