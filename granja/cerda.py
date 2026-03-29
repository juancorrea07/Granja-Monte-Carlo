from embarazo import Embarazo

class Cerda:
    def __init__(self, id, raza, edad, peso):
        self.id = id
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.embarazos = []

    def registrar_embarazo(self, fecha_monta):
        embarazo = Embarazo(fecha_monta)
        self.embarazos.append(embarazo)
        return embarazo

    def obtener_historial(self):
        return self.embarazos

    def __str__(self):
        return f"Cerda {self.id} - Raza: {self.raza}, Edad: {self.edad}, Peso: {self.peso}"