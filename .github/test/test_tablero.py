import unittest
from src.tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
    def test_inicializacion(self):
        for fila in self.tablero.casillas:
            for casilla in fila:
                self.assertEqual(casilla, " ")
    def test_colocar_ficha_exitoso(self):
        resultado = self.tablero.colocar_ficha(1, 1, "X")
        self.assertTrue(resultado)
        self.assertEqual(self.tablero.casillas[1][1], "X")
    def test_colocar_ficha_casilla_ocupada(self):
        self.tablero.colocar_ficha(0, 0, "X")
        resultado = self.tablero.colocar_ficha(0, 0, "O")
        self.assertFalse(resultado)
        self.assertEqual(self.tablero.casillas[0][0], "X")
    def test_verificar_ganador_fila(self):
        for col in range(3):
            self.tablero.colocar_ficha(0, col, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    def test_verificar_ganador_columna(self):
        for fila in range(3):
            self.tablero.colocar_ficha(fila, 0, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))
        self.assertFalse(self.tablero.verificar_ganador("X"))
    def test_verificar_ganador_diagonal_principal(self):
        for i in range(3):
            self.tablero.colocar_ficha(i, i, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))
    def test_verificar_ganador_diagonal_secundaria(self):
        for i in range(3):
            self.tablero.colocar_ficha(i, 2-i, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))
    def test_sin_ganador(self):
        self.tablero.colocar_ficha(0, 0, "X")
        self.tablero.colocar_ficha(1, 1, "O")
        self.assertFalse(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    def test_tablero_vacio_no_lleno(self):
        self.assertFalse(self.tablero.tablero_lleno())
    def test_tablero_parcial_no_lleno(self):
        self.tablero.colocar_ficha(0, 0, "X")
        self.tablero.colocar_ficha(1, 1, "O")
        self.assertFalse(self.tablero.tablero_lleno())
    def test_tablero_lleno_completo(self):
        fichas = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        pos = 0
        for fila in range(3):
            for col in range(3):
                self.tablero.colocar_ficha(fila, col, fichas[pos])
                pos += 1
        self.assertTrue(self.tablero.tablero_lleno())

if __name__ == "__main__":
    unittest.main()