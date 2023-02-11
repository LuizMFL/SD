import Pyro4
class Cliente:
    def __init__(self) -> None:
        calc = Pyro4.Proxy('PYRO:calc@localhost:5500')
        comandos = {
            'sum': calc.sum,
            'sub': calc.sub,
            'mult': calc.mult,
            'div': calc.div,
            'loge': calc.loge,
            'log10': calc.log10,
            'exp': calc.exp,
            'sin': calc.sin,
            'cos': calc.cos,
            'sqrt': calc.sqrt
        }
        print('Operaçoes:')
        print('sum(x,y)')
        print('sub(x,y)')
        print('mult(x,y)')
        print('div(x,y)')
        print('loge(x)')
        print('log10(x)')
        print('exp(x,y)')
        print('sin(x radius)')
        print('cos(x radius)')
        print('sqrt(x)')
        print('-----------------------')
        while True:
            escolha = input('Qual operação: ').replace(' ', '')
            op = ''
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
            a = 0
            if isinstance(constants, list):
                a = comandos[op](constants[0], constants[1])
            else:
                a = comandos[op](constants)
            print(a)
if __name__ == '__main__':
    Cliente()