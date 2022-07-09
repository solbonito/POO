import unittest

"""
Crear la clase Punto en el plano que contiene:
    2 atributos (x, y) que representan las coordenadas del Punto en el plano
    El constructor de la clase Punto que recibe x e y que son las coordenadas
    Por defecto setear x e y en el centro de coordenadas
    Los métodos getter y setter de los atributos
    El método toString()
    Método cuadrante() que devuelve un nro entre 1 y 4 que indica el cuadrante en el cual se encuentra el Punto.
    Método distanciaAlCentro() que devuelve un número que representa la distancia entre el punto y el centro de             
    coordenadas. (x1 - x2) al cuadrado + (y1 - y2) al cuadrado -> aplicar raiz cuadrada

"""

class VerificarDatos(unittest.TestCase):
    def test_cuadrante(self):
        punto_en_el_plano = PuntoEnElPlano()
        punto_en_el_plano.set_punto_coordenada_x(5)
        punto_en_el_plano.set_punto_coordenada_y(3)
        self.assertEqual(punto_en_el_plano.cuadrante(), 1)


class PuntoEnElPlano:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def cuadrante(self):
        if self.x>0 and self.y>0:
            return 1
        elif self.x<0 and self.y>0:
            return 2
        elif self.x<0 and self.y<0:
            return 3
        elif self.x>0 and self.y<0:
            return 4
        else:
            return "El punto se encuentra en el centro de coordenadas"

    def distancia_al_centro(self,punto):
        return ((self.x - punto.x)**2 + (self.y - punto.y)**2) ** 1/2

    def set_punto_coordenada_x(self,x):
        self.x = x

    def set_punto_coordenada_y(self,y):
        self.y = y

    def get_punto_coordenada_x(self,x):
        self.x = x
        
    def get_punto_coordenada_y(self,y):
        self.y = y

    def __str__(self):
        return "Coordenada x: {}\nCoordenada y: {}\nCuadrante: {}".format(self.x,self.y,self.cuadrante())


if __name__=="__main__":
    unittest.main()