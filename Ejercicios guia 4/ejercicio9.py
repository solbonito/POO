import unittest
"""
Se solicita implementar una o varias clases que nos permita controlar un tablero electronico de basquet, por lo tanto:
Crear una clase TableroDeBasquet el cual tendrá como atributos: local (string), visitante (string), puntos_local (entero),
y puntos_visitante (entero).
Crear un método que adicione puntos de a 3, tanto al local como al visitante
Crear un método que adicione puntos de a 2, tanto al local como al visitante.
Crear un método que adicione puntos de a 1, tanto al local como al visitante.
"""


class VerificarTableroDeBasquet(unittest.TestCase):
    def test_suma_3puntos(self):
        tablero = TableroDeBasquet("Boca", "River", 4, 7)
        self.assertTrue(tablero.suma_3puntos(),"Puntos local: 7, Puntos visitante: 10")

    def test_suma_2puntos(self):
        tablero = TableroDeBasquet("Boca","River",9,7)
        self.assertTrue(tablero.suma_2puntos(),"Puntos local: 11, Puntos visitante: 9")
        
    def test_suma_1puntos(self):
        tablero = TableroDeBasquet("Boca","River",0,0)
        self.assertTrue(tablero.suma_1punto(),"Puntos local: 1, Puntos visitante: 1")
        
class TableroDeBasquet:
    def __init__(self,local,visitante,puntos_local,puntos_visitante):
        self.local = local
        self.visitante = visitante
        self.puntos_local = puntos_local
        self.puntos_visitante = puntos_visitante

    def suma_3puntos(self):
        self.puntos_local+=3
        self.puntos_visitante+=3
        return "Puntos equipo local: {}\mPuntos equipo visitante: {}".format(self.puntos_local,self.puntos_visitante)
        
    def suma_2puntos(self):
        self.puntos_local+=2
        self.puntos_visitante+=2
        return "Puntos equipo local: {}\mPuntos equipo visitante: {}".format(self.puntos_local,self.puntos_visitante)
        

    def suma_1punto(self):
        self.puntos_local+=1
        self.puntos_visitante+=1
        return "Puntos equipo local: {}\mPuntos equipo visitante: {}".format(self.puntos_local,self.puntos_visitante)
        
    def get_local(self):
        return self.local
    
    def get_visitante(self):
        return self.visitante
    
    def get_puntos_local(self):
        return self.puntos_local
    
    def get_puntos_visitante(self):
        return self.puntos_visitante
    
    def set_local(self,local):
        self.local = local
    
    def set_visitante(self,visitante):
        self.visitante = visitante
    
    def set_puntos_local(self,puntos):
        self.puntos_local = puntos
        
    def set_puntos_visitante(self,puntos):
        self.puntos_visitante = puntos

    def __str__(self):
        return "Equipo local: {}\nPuntos: {}\nEquipo visitante: {}\nPuntos: {}".format(self.local,self.puntos_local,self.visitante,self.puntos_visitante)



if __name__== "__main__":
    unittest.main()
    


