import unittest
"""
Agregue una mejora o funcionalidad a la calculadora, por ejemplo: que se pueda acumular el resultado 
y seguir realizando operaciones, calcular la potencia de 2 de un número, calcular el factorial de un número, etc.
"""

class ProbarCalculadora(unittest.TestCase):
    def test_potencia(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.potencia(5,2),25)
    
    def test_raiz(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.raiz(25,2),5)
        
        
class Calculadora:
    def potencia(self,num,potencia):
        return num ** potencia
    
    def raiz(self,num,raiz):
        return num ** (1/raiz)

if __name__=="__main__":
   unittest.main()