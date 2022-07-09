import unittest
import ejercicio6
"""
Crear la clase Segmento que contiene:
    2 atributos del tipo Punto que representan los extremos del Segmento,
    El constructor de la clase Segmento que recibe dos parámetros del tipo Punto para los extremos
    Los métodos getter y setter de los atributos
    El método toString()
    Un método longitudSegmento() que devuelve un número float que representa la longitud del segmento
"""
class VerificarDatosSegmento (unittest.TestCase):
    def test_longitud_segmento(self):
        puntoA = ejercicio6.PuntoEnElPlano(5,3)
        puntoB = ejercicio6.PuntoEnElPlano(2,6)
        segmento = Segmento(puntoA,puntoB)
        self.assertEqual(segmento.longitud_segmento(),9.0)
          
class Segmento:
    def __init__(self,puntoA,puntoB):
        self.puntoA = puntoA
        self.puntoB = puntoB

    def longitud_segmento(self):
        return ejercicio6.PuntoEnElPlano.distancia_al_centro(self.puntoA,self.puntoB)
        
    def set_puntoA(self,puntoA):
        self.puntoA = puntoA
        
    def set_puntoB(self,puntoB):
        self.puntoB = puntoB
    
    def get_puntoA(self):
        self.puntoA
        
    def get_puntoB(self):
        self.puntoB
        
    def __str__(self):
        return "Punto A: \n{}\nPunto B: \n{}\nLongitud del segmento: {}".format(self.puntoA,self.puntoB,self.longitud_segmento())
         

if __name__=="__main__":
   unittest.main()