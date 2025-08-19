import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from src.tablero import Tablero
from src.jugador import Jugador
from src.cli import pedir_posicion, mostrar_mensaje

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
    def test_inicializacion(self):
        self.assertEqual(len(self.tablero.casillas), 3)
        self.assertEqual(len(self.tablero.casillas[0]), 3)
        for fila in self.tablero.casillas:
            for casilla in fila:
                self.assertEqual(casilla, " ")
    def test_colocar_ficha_valida(self):
        resultado = self.tablero.colocar_ficha(0, 0, "X")
        self.assertTrue(resultado)
        self.assertEqual(self.tablero.casillas[0][0], "X")
    def test_colocar_ficha_ocupada(self):
        self.tablero.colocar_ficha(0, 0, "X")
        resultado = self.tablero.colocar_ficha(0, 0, "O")
        self.assertFalse(resultado)
        self.assertEqual(self.tablero.casillas[0][0], "X")
    def test_verificar_ganador_fila(self):
        for j in range(3):
            self.tablero.casillas[0][j] = "X"
        self.assertTrue(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    def test_verificar_ganador_columna(self):
        for i in range(3):
            self.tablero.casillas[i][0] = "O"
        self.assertTrue(self.tablero.verificar_ganador("O"))
        self.assertFalse(self.tablero.verificar_ganador("X"))
    def test_verificar_ganador_diagonal_principal(self):
        for i in range(3):
            self.tablero.casillas[i][i] = "X"
        self.assertTrue(self.tablero.verificar_ganador("X"))
    def test_verificar_ganador_diagonal_secundaria(self):
        for i in range(3):
            self.tablero.casillas[i][2-i] = "O"
        self.assertTrue(self.tablero.verificar_ganador("O"))
    def test_no_ganador(self):
        self.tablero.casillas[0][0] = "X"
        self.tablero.casillas[1][1] = "O"
        self.assertFalse(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    def test_tablero_lleno(self):
        fichas = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        idx = 0
        for i in range(3):
            for j in range(3):
                self.tablero.casillas[i][j] = fichas[idx]
                idx += 1
        self.assertTrue(self.tablero.tablero_lleno())
    def test_tablero_no_lleno(self):
        self.tablero.casillas[0][0] = "X"
        self.assertFalse(self.tablero.tablero_lleno())
    @patch('builtins.print')
    def test_mostrar(self, mock_print):
        self.tablero.casillas[0][0] = "X"
        self.tablero.casillas[1][1] = "O"
        self.tablero.mostrar()
        self.assertTrue(mock_print.called)

class TestJugador(unittest.TestCase):
    def setUp(self):
        self.jugador = Jugador("Test", "X")
    def test_inicializacion(self):
        self.assertEqual(self.jugador.nombre, "Test")
        self.assertEqual(self.jugador.ficha, "X")
        self.assertEqual(self.jugador.fichas_colocadas, 0)
        self.assertEqual(self.jugador.max_fichas, 3)
    def test_puede_colocar_inicial(self):
        self.assertTrue(self.jugador.puede_colocar())
    def test_colocar_ficha(self):
        resultado = self.jugador.colocar_ficha()
        self.assertTrue(resultado)
        self.assertEqual(self.jugador.fichas_colocadas, 1)
    def test_limite_fichas(self):
        for _ in range(3):
            self.jugador.colocar_ficha()
        self.assertFalse(self.jugador.puede_colocar())
        resultado = self.jugador.colocar_ficha()
        self.assertFalse(resultado)
        self.assertEqual(self.jugador.fichas_colocadas, 3)

class TestCLI(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2'])
    def test_pedir_posicion_valida(self, mock_input):
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)
    @patch('builtins.input', side_effect=['q'])
    def test_pedir_posicion_salir_q(self, mock_input):
        fila, columna = pedir_posicion()
        self.assertIsNone(fila)
        self.assertIsNone(columna)
    @patch('builtins.input', side_effect=['salir'])
    def test_pedir_posicion_salir_palabra(self, mock_input):
        fila, columna = pedir_posicion()
        self.assertIsNone(fila)
        self.assertIsNone(columna)
    @patch('builtins.input', side_effect=['1', 'q'])
    def test_pedir_posicion_salir_columna(self, mock_input):
        fila, columna = pedir_posicion()
        self.assertIsNone(fila)
        self.assertIsNone(columna)
    @patch('builtins.print')
    def test_mostrar_mensaje(self, mock_print):
        mensaje = "Test message"
        mostrar_mensaje(mensaje)
        mock_print.assert_called_once_with(mensaje)

class TestJuegoIntegracion(unittest.TestCase):
    def test_tablero_con_jugadores(self):
        tablero = Tablero()
        jugador1 = Jugador("Jugador 1", "X")
        jugador2 = Jugador("Jugador 2", "O")
        self.assertTrue(tablero.colocar_ficha(0, 0, jugador1.ficha))
        self.assertTrue(tablero.colocar_ficha(0, 1, jugador2.ficha))
        self.assertTrue(tablero.colocar_ficha(1, 1, jugador1.ficha))
        self.assertEqual(tablero.casillas[0][0], "X")
        self.assertEqual(tablero.casillas[0][1], "O")
        self.assertEqual(tablero.casillas[1][1], "X")
    def test_secuencia_ganadora(self):
        tablero = Tablero()
        jugador = Jugador("Test", "X")
        tablero.colocar_ficha(0, 0, jugador.ficha)
        tablero.colocar_ficha(0, 1, jugador.ficha)
        tablero.colocar_ficha(0, 2, jugador.ficha)
        self.assertTrue(tablero.verificar_ganador(jugador.ficha))
    def test_tablero_completo_empate(self):
        tablero = Tablero()
        movimientos = [
            (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
            (1, 0, "O"), (1, 1, "X"), (1, 2, "O"),
            (2, 0, "O"), (2, 1, "X"), (2, 2, "O")
        ]
        for fila, col, ficha in movimientos:
            tablero.colocar_ficha(fila, col, ficha)
        self.assertTrue(tablero.tablero_lleno())
        self.assertFalse(tablero.verificar_ganador("X"))
        self.assertFalse(tablero.verificar_ganador("O"))

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, timeout=30)