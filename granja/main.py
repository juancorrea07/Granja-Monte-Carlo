from datetime import datetime
from granja import Granja
from cerda import Cerda
from parto import Parto

granja = Granja()

def menu():
    while True:
        print("\n--- SISTEMA GRANJA PORCINA ---")
        print("1. Registrar cerda")
        print("2. Registrar embarazo")
        print("3. Registrar parto")
        print("4. Ver historial")
        print("5. Ver estadísticas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            raza = input("Raza: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso: "))
            cerda = Cerda(id, raza, edad, peso)
            granja.agregar_cerda(cerda)

        elif opcion == "2":
            id = input("ID de la cerda: ")
            cerda = granja.buscar_cerda(id)

            if cerda:
                fecha = datetime.strptime(input("Fecha de monta (YYYY-MM-DD): "), "%Y-%m-%d")
                embarazo = cerda.registrar_embarazo(fecha)
                print("Fecha probable de parto:", embarazo.fecha_probable_parto)
            else:
                print("Cerda no encontrada.")

        elif opcion == "3":
            id = input("ID de la cerda: ")
            cerda = granja.buscar_cerda(id)

            if cerda and cerda.embarazos:
                embarazo = cerda.embarazos[-1]  # último embarazo
                fecha = datetime.strptime(input("Fecha de parto: "), "%Y-%m-%d")
                nacidos = int(input("Lechones nacidos: "))
                vivos = int(input("Lechones vivos: "))

                parto = Parto(fecha, nacidos, vivos)
                embarazo.registrar_parto(parto)
                print("Parto registrado.")
            else:
                print("No hay embarazo registrado.")

        elif opcion == "4":
            id = input("ID de la cerda: ")
            cerda = granja.buscar_cerda(id)

            if cerda:
                for e in cerda.embarazos:
                    print(e)
                    if e.parto:
                        print("  ", e.parto)
            else:
                print("Cerda no encontrada.")

        elif opcion == "5":
            granja.generar_estadisticas()

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")

menu()