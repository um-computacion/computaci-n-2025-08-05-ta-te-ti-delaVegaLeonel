class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return f"{self.nombre} ({self.ficha})"

    def puede_colocar_ficha(self, ficha):
        return self.ficha_colocada < self.max_fichas_colocadas
    
    def colocar_ficha(self):
        if self.puede_colocar():
            self.fichas_colocadas += 1
            return True
        return False