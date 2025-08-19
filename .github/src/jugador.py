from tablero import Tablero

class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
        self.ficha_colocada = 0
        self.max_fichas_colocadas = 3
        self.tablero = Tablero()


    def puede_colocar_ficha(self, ficha):
        return self.ficha_colocada < self.max_fichas_colocadas
    
    def colocar_ficha(self):
        if self.puede_colocar():
            self.fichas_colocadas += 1
            return True
        return False