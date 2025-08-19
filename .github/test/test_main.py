import unittest
from unittest.mock import patch
import io
import sys
import main

class TestMain(unittest.TestCase):
    @patch("src.tateti.jugar")
    def test_main_llama_jugar(self, mock_jugar):
        # Capturamos salida
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Ejecutamos el main como si fuera desde consola
        with patch("builtins.print") as mock_print:
            main.__name__ = "__main__"  # Simular ejecución directa
            with patch("builtins.exit", side_effect=SystemExit):
                try:
                    # Forzamos ejecución del bloque if __name__ == "__main__":
                    exec(open("main.py").read(), {"__name__": "__main__"})
                except SystemExit:
                    pass

            mock_jugar.assert_called_once()
            mock_print.assert_any_call("=== Bienvenido al juego de Ta-Te-Ti ===")

        sys.stdout = sys.__stdout__
