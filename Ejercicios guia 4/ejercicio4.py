import unittest
"""
EJERCICIO DIFERENCIA ENTRE POO Y ESTRUCTURADA: con programación estructurada 
realice un programa que permita agregar notas a un estudiante y se pueda calcular 
el promedio de notas de cada estudiante. 
El alumno posee como datos nombre (string), apellido (string), nro de legajo (entero), 
notas (sería una lista o array de numeros con decimal). 
"""
        
def cargar_datos(nombre,apellido,legajo,notas):
    estudiante = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Nro. de Legajo": legajo,
        "Notas": notas
    }
    
    return estudiante

def calcular_promedio(estudiante):
    suma = 0
    cant_notas = 0
    for nota in estudiante["Notas"]:
        suma += nota
        cant_notas += 1
    
    return suma / cant_notas

def mostrar_datos(estudiante):
    for key in estudiante:
        print(("{}: {}").format(key,estudiante[key]))

"""
¿Qué dificultades hubo para realizar la implementación? 
        Dificultades en sí ninguna
"""
"""
¿Cómo podriamos implementarlo con objetos y clases? Implementar una solución. 
Hacer tests unitarios solamente del ejercicio hecho con POO
"""
class DatosEstudiante(unittest.TestCase):
    def test_cargar_nota(self):
        estudiante = Estudiante("Mario","Gómez",22046)
        estudiante.cargar_notas(7.5)
        self.assertEqual(estudiante.notas, [7.5])
                      
    def test_calcular_promedio(self):
        estudiante = Estudiante("Mario","Gómez",22046)
        estudiante.set_notas([7.5,6,9.5,3]) 
        self.assertEqual(estudiante.calcular_promedio(), 6.5)
        
          
class Estudiante:
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.notas = []
        
    def cargar_notas(self,nota):
        self.notas.append(nota)
        
    def calcular_promedio(self):
        sum_notas = 0
        cant_notas = 0
        
        for nota in self.notas:
            sum_notas+=nota
            cant_notas+=1
        
        return sum_notas/cant_notas
    
    def set_notas(self,notas):
        self.notas = notas       
      
    def __str__(self):
        return "Nombre: {}\nApellido: {}\nLegajo: {}\nPromedio:{}".format(self.nombre,self.apellido,self.legajo,self.calcular_promedio)
    
    

"""
¿Qué pasaría si tuviesemos que agregar más información, notas por materia, 
datos acerca de los pagos de matrícula y cuotas, sanciones disciplinarias, 
asistencia, etc? Responder sin implementar o analizar posibles soluciones.

    Para agregar notas por materia se puede hacer uso de un método que maneje diccionarios. 
    Para cualquier otra información la respuesta en sí es lo mismo, se agrega un método/atributos a la clase.  
"""

    
if __name__ == "__main__":
    unittest.main()