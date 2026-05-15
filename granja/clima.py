import requests

def obtener_clima(ciudad):
    api_key = "3b8b3f2455349c877db65b86f85b808e"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        data = respuesta.json()

        if respuesta.status_code == 200:
            return {
                "ciudad": ciudad,
                "temperatura": data["main"]["temp"],
                "humedad": data["main"]["humidity"],
                "descripcion": data["weather"][0]["description"]
            }
        else:
            print("Error:", data.get("message"))
            return None

    except Exception as e:
        print("Error de conexión:", e)
        return None

def mostrar_clima_granja(ciudad):
    clima = obtener_clima(ciudad)
    if clima is None:
        return None
    else:
        print("\n--- CLIMA EN LA GRANJA ---")
        print(f"Ciudad: {clima['ciudad']}")
        print(f"Temperatura: {clima['temperatura']} °C")
        print(f"Humedad: {clima['humedad']}%")
        print(f"Condición: {clima['descripcion']}")

        print("\n--- ANÁLISIS ---")

        temp = clima["temperatura"]

        if temp > 30:
            print("Alerta: Temperatura alta. Riesgo de estrés térmico en las cerdas.")
        elif temp < 15:
            print("Alerta: Temperatura baja. Revisar condiciones de abrigo.")
        else:
            print("Condiciones climáticas adecuadas para la granja.")


