import unittest
"""
 Crear una función que tome un array de numeros y retorne la palabra “Boom!” si el dígito 7 aparece en el array. Sino, que retorne “No se encuentra el número 7 en el array” .
Ejemplo:
    sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!" // El array contiene el número 7
    sevenBoom([8, 6, 33, 100]) ➞ “No se encuentra el número 7 en el array” // ninguno de los elementos contiene el número 7
    sevenBoom([2, 55, 60, 97, 86]) ➞ "Boom!" // 97 contiene el número 7.
"""
class VerificarNumero7TestCase(unittest.TestCase):
    def test_numero7_esta_en_array(self):
        self.assertEqual(seven_boom([1, 2, 3, 4, 5, 6, 7]), "Boom!")

    def test_numero7_no_esta_en_array(self):
        self.assertEqual(seven_boom([8, 6, 33, 100]),
                         "No se encuentra el número 7 en el array")
        
def seven_boom(array):
    if 7 in array:
        resultado = "Boom!"
    else:
        resultado = "No se encuentra el número 7 en el array"

    return resultado


if __name__ == '__main__':
    unittest.main()