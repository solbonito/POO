import unittest
"""
Ejercicio 12: Escribir una función recursiva que reciba un conjunto de caracteres únicos, y un número K, 
e imprima todas las posibles cadenas de longitud K 
formadas con los caracteres dados (permitiendo caracteres repetidos).
Ejemplo:
    combinaciones(['a', 'b', 'c'], 2) debe imprimir aa ab ac ba bb bc ca cb cc

"""
class CombinarCaracteresTestCase(unittest.TestCase):
    def test_combinaciones_longitud_cadena_2(self):
        self.assertEqual(combinar_caracteres(['a', 'b', 'c'], 2),"aa ab ac ba bb bc ca cb cc")

def combinar_caracteres(lista,longitud):
    resultado = ""
    
    if longitud == 0:      
        resultado+= lista[(len(lista)-1)-longitud] + lista[0] + " "
        resultado+= lista[(len(lista)-1)-longitud] + lista[1] + " " 
        resultado+= lista[(len(lista)-1)-longitud] + lista[2]
    else:
        resultado+= lista[(len(lista)-1)-longitud] + lista[0] + " "
        resultado+= lista[(len(lista)-1)-longitud] + lista[1] + " " 
        resultado+= lista[(len(lista)-1)-longitud] + lista[2] + " " + combinar_caracteres(lista,longitud-1) 

    return resultado


if __name__ == '__main__':
    unittest.main()