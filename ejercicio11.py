import unittest
"""
Escribí una función que reciba dos parámetros: un string S y un integer R. La función debe devolver un string donde los caracteres consecutivos de S no se repitan más que R veces.
Tiene que devolver un string con el texto limpio y la cantidad de caracteres repetidos correcta.

Ejemplos:
    "AAA", 2 => "AA"
    "AAAAAFFFFOOOA", 2 => "AAFFOOA"
    "111223333344", 1 => "1234"
    "AABB", 1 => "AB"
"""

class RepetirCaracteresTestCase(unittest.TestCase):
    def test_2_repeticiones(self):
        self.assertEqual(repetir_caracteres("AAAAAFFFFOOOA", 2),"AAFFOOA")
        
    def test_1_repeticion(self):
        self.assertEqual(repetir_caracteres("111223333344", 1),"1234")
	
def repetir_caracteres(string,repeticiones):
    resultado = ""
    contador = 0

    for caracter in string:
        if contador != repeticiones:
            resultado+=caracter
            contador += 1
        elif caracter != resultado[-1]:
            contador = 0
            resultado+=caracter
            contador += 1
       
    return resultado


if __name__ == '__main__':
    unittest.main()