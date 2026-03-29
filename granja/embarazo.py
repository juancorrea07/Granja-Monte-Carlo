from datetime import timedelta
from parto import Parto

class Embarazo:
    def __init__(self, fecha_monta):
        self.fecha_monta = fecha_monta
        self.fecha_probable_parto = self.calcular_fecha_parto()
        self.parto = None

    def calcular_fecha_parto(self):
        return self.fecha_monta + timedelta(days=114)

    def registrar_parto(self, parto):
        if self.parto is None:
            self.parto = parto
        else:
            print("Este embarazo ya tiene un parto registrado.")

    def __str__(self):
        return f"Embarazo - Monta: {self.fecha_monta}, Parto estimado: {self.fecha_probable_parto}"