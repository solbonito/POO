import unittest
"""
Crear una clase Calculadora que pueda realizar las acciones de sumar, multiplicar, dividir y restar.
Diseñar al menos 2 test unitarios.
"""

class ProbarCalculadora(unittest.TestCase):
    def test_sumar(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.sumar(17,3),20)
        
    def test_multiplicar(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.multiplicar(10,3),30)

    def test_dividir(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.dividir(15,3),5)

    def test_restar(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.restar(60,10),50)


class Calculadora:
    def sumar(self,num1,num2):
        return num1+num2
        
    def multiplicar(self,num1,num2):
        return num1*num2
    
    def dividir(self,num1,num2):
        if num1 and num2 > 0:
            return num1 / num2
                
    def restar(self,num1,num2):
        return num1-num2


if __name__=="__main__":
   unittest.main()