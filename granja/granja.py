class Granja:
    def __init__(self):
        self.cerdas = []

    def agregar_cerda(self, cerda):
        if self.buscar_cerda(cerda.id) is None:
            self.cerdas.append(cerda)
            print("Cerda registrada correctamente.")
        else:
            print("Error: Ya existe una cerda con ese ID.")

    def buscar_cerda(self, id):
        for cerda in self.cerdas:
            if cerda.id == id:
                return cerda
        return None

    def generar_estadisticas(self):
        total_partos = 0
        total_lechones = 0
        total_vivos = 0

        for cerda in self.cerdas:
            for embarazo in cerda.embarazos:
                if embarazo.parto:
                    total_partos += 1
                    total_lechones += embarazo.parto.lechones_nacidos
                    total_vivos += embarazo.parto.lechones_vivos

        if total_partos == 0:
            print("No hay datos suficientes.")
            return

        promedio = total_lechones / total_partos
        tasa = (total_vivos / total_lechones) * 100

        print(f"Promedio de lechones por parto: {promedio}")
        print(f"Tasa de supervivencia: {tasa:.2f}%")