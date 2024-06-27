#CLASE DE OPERACIONES ARITMETICAS

import os
os.system('cls' if os.name == 'nt' else 'clear')

class OperacionesAritmeticas:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #SUMA
    def suma(self):
        print(self.a+self.b)
    
    def potencia(self,a,b):
        print(a**b)


op=OperacionesAritmeticas(int(input("a: "),int(input("b: "))))
op.suma()
op.potencia(5,5)
op.suma()