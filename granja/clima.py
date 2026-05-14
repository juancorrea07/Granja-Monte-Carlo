import requests


def obtener_clima():
    ciudad = input("Ingrese la ciudad: ")
    obtener_clima(ciudad)
    api_key = "3b8b3f2455349c877db65b86f85b808e"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        data = respuesta.json()

        if respuesta.status_code == 200:
            temperatura = data["main"]["temp"]
            humedad = data["main"]["humidity"]
            descripcion = data["weather"][0]["description"]

            print("\n--- CLIMA ACTUAL ---")
            print(f"Ciudad: {ciudad}")
            print(f"Temperatura: {temperatura} °C")
            print(f"Humedad: {humedad}%")
            print(f"Condición: {descripcion}")
        else:
            print("Error al obtener el clima:", data.get("message"))

    except Exception as e:
        print("Error de conexión:", e)