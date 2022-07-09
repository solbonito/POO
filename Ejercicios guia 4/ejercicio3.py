import unittest

"""
Crear una clase lampara con un metodo para cambiar su estado 
(si estaba apagada pasa a estar prendida y viceversa). 
"""

class EstadoLampara(unittest.TestCase):
    def test_cambiar_estado(self):
        lampara = Lampara("prendida")
        self.assertEqual(lampara.cambiar_estado(),"apagada")
        
class Lampara:
    def __init__(self,estado):
        self.estado = estado
        
    def cambiar_estado(self):
        if self.estado == "prendida":
            self.estado = "apagada"
        else:
            self.estado = "prendida"
        
        return self.estado
    
    def __str__(self):
        return "La lámpara está: {}".format(self.estado)
    
if __name__ == "__main__":
    unittest.main()