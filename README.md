

## Requisitos funcionales

### R1 – Registrar nueva cerda
Permite registrar una cerda con su ID, raza, edad y peso, validando que el ID no esté duplicado.

### R2 – Registrar embarazo
Permite registrar la fecha de monta de una cerda y calcular automáticamente la fecha probable de parto (114 días).

### R3 – Registrar parto
Permite registrar el parto de una cerda con el número de lechones nacidos y vivos.

### R4 – Consultar historial
Permite visualizar el historial completo de embarazos y partos de una cerda.

### R5 – Generar estadísticas
Permite calcular el promedio de lechones por parto y la tasa de supervivencia.



## Estructura del proyecto

```
granja/
│
├── cerda.py
├── embarazo.py
├── parto.py
├── granja.py
├── main.py
```

---

## Diagrama de clases (UML)

```mermaid
classDiagram

class Granja {
    - cerdas: List<Cerda>
    + agregar_cerda(cerda: Cerda)
    + buscar_cerda(id: str): Cerda
    + generar_estadisticas(): void
}

class Cerda {
    - id: str
    - raza: str
    - edad: int
    - peso: float
    - embarazos: List<Embarazo>
    + registrar_embarazo(fecha_monta: date): Embarazo
    + obtener_historial(): List<Embarazo>
}

class Embarazo {
    - fecha_monta: date
    - fecha_probable_parto: date
    - parto: Parto
    + calcular_fecha_parto(): date
    + registrar_parto(parto: Parto): void
}

class Parto {
    - fecha: date
    - lechones_nacidos: int
    - lechones_vivos: int
    + calcular_supervivencia(): float
}

Granja "1" *-- "0..*" Cerda : contiene
Cerda "1" --> "0..*" Embarazo : tiene
Embarazo "1" --> "0..1" Parto : genera
```

---
