from datetime import datetime

class Parto:
    def __init__(self, fecha, lechones_nacidos, lechones_vivos):
        self.fecha = fecha
        self.lechones_nacidos = lechones_nacidos
        self.lechones_vivos = lechones_vivos

    def calcular_supervivencia(self):
        if self.lechones_nacidos == 0:
            return 0
        return (self.lechones_vivos / self.lechones_nacidos) * 100

    def __str__(self):
        return f"Parto - Fecha: {self.fecha}, Nacidos: {self.lechones_nacidos}, Vivos: {self.lechones_vivos}"