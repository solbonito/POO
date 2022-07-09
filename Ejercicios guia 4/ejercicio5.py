import unittest
"""
Crear una clase Rectángulo, con atributos base y altura. 
Crear también el constructor de la clase y los métodos necesarios para calcular el área y el perímetro. 
La fórmula del área es base*altura y el perímetro 2*base + 2*altura
"""
class VerificarDatos(unittest.TestCase):
    def test_calcular_area_rectangulo(self):
        rectangulo = Rectangulo(5,3)
        self.assertEqual(rectangulo.calcular_area(), 15)

    def test_calcular_perimetro_rectangulo(self):
        rectangulo = Rectangulo(5,3)
        self.assertEqual(rectangulo.calcular_perimetro(), 16)
        
class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura    

    def calcular_area(self):
        area = self.base*self.altura
        return area

    def calcular_perimetro(self):
        perimetro = 2*self.base + 2*self.altura
        return perimetro 
    
    
if __name__=="__main__":
    unittest.main()