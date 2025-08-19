import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    
    def setUp(self):
        self.jugador_x = Jugador("Ana", "X")
        self.jugador_o = Jugador("Luis", "O")
    
    def test_inicializacion(self):
        self.assertEqual(self.jugador_x.nombre, "Ana")
        self.assertEqual(self.jugador_x.ficha, "X")
        self.assertEqual(self.jugador_x.fichas_colocadas, 0)
        self.assertEqual(self.jugador_x.max_fichas, 3)
        self.assertEqual(self.jugador_o.nombre, "Luis")
        self.assertEqual(self.jugador_o.ficha, "O")
    
    def test_puede_colocar_inicial(self):
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_o.puede_colocar())
    
    def test_colocar_ficha_exitoso(self):
        self.assertTrue(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 1)
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 2)
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 3)
        self.assertFalse(self.jugador_x.puede_colocar())
    
    def test_colocar_ficha_limite_alcanzado(self):
        for _ in range(3):
            self.jugador_x.colocar_ficha()
        self.assertFalse(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 3)
        self.assertFalse(self.jugador_x.puede_colocar())
    
    def test_puede_colocar_con_fichas_parciales(self):
        self.assertTrue(self.jugador_x.puede_colocar())
        self.jugador_x.colocar_ficha()
        self.assertTrue(self.jugador_x.puede_colocar())
        self.jugador_x.colocar_ficha()
        self.assertTrue(self.jugador_x.puede_colocar())
        self.jugador_x.colocar_ficha()
        self.assertFalse(self.jugador_x.puede_colocar())
    
    def test_diferentes_jugadores_independientes(self):
        self.jugador_x.colocar_ficha()
        self.jugador_x.colocar_ficha()
        self.jugador_o.colocar_ficha()
        self.assertEqual(self.jugador_x.fichas_colocadas, 2)
        self.assertEqual(self.jugador_o.fichas_colocadas, 1)
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_o.puede_colocar())

if __name__ == '__main__':
    unittest.main()