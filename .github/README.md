Ta-Te-Ti en Python

Un juego Ta-Te-Ti implementado en Python.
Está diseñado en forma modular y con tests unitarios, para que el código sea fácil de mantenerprobar.
Cómo funciona el proyecto


1. tablero.py

Contiene la clase Tablero.
Se encarga de manejar el estado del juego:
Representa un tablero 3x3 en forma de lista de listas.
Permite colocar fichas (X u O) en posiciones vacías.
Comprueba si un jugador ha ganado (filas, columnas y diagonales).
Comprueba si el tablero está lleno (empate).
Muestra el tablero en consola.

2. jugador.py
Define la clase Jugador.
Cada jugador tiene:
nombre → Identificación del jugador.
ficha → Símbolo que usa en el tablero (X u O).
Control opcional de cantidad de fichas colocadas (útil si se quiere extender a versiones con límite de fichas).
Tiene métodos como:
puede_colocar() → Determina si el jugador todavía puede poner fichas.
colocar_ficha() → Aumenta el contador de fichas si puede jugar.

3. cli.py
Maneja la interacción con el usuario en consola.
Funciones principales:
pedir_posicion() → Solicita fila y columna al usuario, valida que sea correcta o que elija salir (q o salir).
mostrar_mensaje(mensaje) → Imprime mensajes en pantalla.

4. tateti.py
Contiene la función (o clase) que controla la lógica principal del juego:
Inicializa el tablero y los jugadores.
Alterna turnos entre jugador X y jugador O.
Llama a cli para pedir posiciones y mostrar mensajes.
Actualiza el tablero y revisa si hay un ganador o un empate.

5. main.py
Es el punto de entrada del proyecto.
Solo muestra un mensaje de bienvenida y llama al motor del juego.
Cómo funciona el proyecto

6. tests/
Contiene todos los tests unitarios escritos con unittest.
Se testean de forma independiente:
El tablero (test_tablero.py).
El jugador (test_jugador.py).
La entrada/salida por consola (test_cli.py).
La lógica de integración (test_tateti.py).
El main.py para verificar que efectivamente llama al juego (test_main.py).

Cómo jugar
Ejecuta:
        python main.py
Luego:
Ingresa la fila y columna donde quieras colocar tu ficha (X o O).
Si ingresas q o salir, el juego termina.
El sistema detecta automáticamente si alguien ganó o si hubo empate.
