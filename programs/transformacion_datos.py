import pandas as pd
import re


def transformar_datos(ruta_csv):
    # Leer el archivo CSV
    df = pd.read_csv(ruta_csv)
    print("=== Datos originales ===")
    print(df)
    print()

    # Transformacion 1: Estandarizar fechas al formato YYYY-MM-DD
    # Fue necesaria porque hay 3 formatos distintos: 2025-01-05, 05/01/2025, 2025/01/18
    # Se creo una funcion que intenta cada formato hasta encontrar el correcto
    from datetime import datetime

    def parse_fecha(fecha):
        formatos = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"]
        for fmt in formatos:
            try:
                return datetime.strptime(str(fecha), fmt)
            except ValueError:
                continue
        return fecha

    df["fecha"] = df["fecha"].apply(parse_fecha)
    print("=== Fechas estandarizadas ===")
    print(df["fecha"])
    print()

    # Transformacion 2: Limpiar espacios en blanco en ciudades
    # Fue necesaria porque habia ciudades con espacios como " CDMX " y "Monterrey "
    df["ciudad"] = df["ciudad"].str.strip()
    print("=== Ciudades limpias ===")
    print(df["ciudad"].unique())
    print()

    # Transformacion 3: Estandarizar categorias
    # Fue necesaria porque habia variaciones como "Tecnologia", "TEC", "tecnologia"
    mapeo_categorias = {
        "Tecnologia": "Tecnologia",
        "TEC": "Tecnologia",
        "tecnologia": "Tecnologia",
        "Hogar": "Hogar",
        "Ropa": "Ropa",
    }
    df["categoria"] = df["categoria"].map(mapeo_categorias)
    print("=== Categorias estandarizadas ===")
    print(df["categoria"].unique())
    print()

    # Transformacion 4: Estandarizar genero a valores cortos (F, M)
    # Fue necesaria porque habia "Femenino", "Masculino", "m", "F", "M"
    mapeo_genero = {
        "F": "F",
        "M": "M",
        "Masculino": "M",
        "Femenino": "F",
        "m": "M",
    }
    df["genero"] = df["genero"].map(mapeo_genero)
    print("=== Genero estandarizado ===")
    print(df["genero"].value_counts())
    print()

    # Transformacion 5: Limpiar columna cantidad
    # Fue necesaria porque habia valores como "1 pieza", "2 piezas" y NaN mezclados con numeros
    # Se uso regex para extraer solo el numero, y se lleno NaN con 1 antes de convertir
    df["cantidad"] = df["cantidad"].fillna(1)
    df["cantidad"] = df["cantidad"].astype(str).apply(
        lambda x: int(re.search(r"\d+", x).group())
    )
    print("=== Cantidad limpia ===")
    print(df["cantidad"])
    print()

    # Transformacion 6: Llenar valores vacios en genero con la moda
    # Fue necesaria porque la fila 39 (Erika Campos) tenia genero vacio
    df["genero"] = df["genero"].fillna(df["genero"].mode()[0])
    print("=== Genero despues de llenar NaN ===")
    print(df["genero"].value_counts())
    print()

    # Transformacion 7: Llenar producto vacio con "Sin nombre"
    # Fue necesaria porque la fila 36 tenia producto vacio
    df["producto"] = df["producto"].fillna("Sin nombre")
    print("=== Producto despues de llenar NaN ===")
    print(df[df["producto"] == "Sin nombre"])
    print()

    # Transformacion 8: Crear columna venta_total (precio * cantidad)
    # Fue necesaria para tener el monto total de cada venta y facilitar analisis posteriores
    df["venta_total"] = df["precio"] * df["cantidad"]
    print("=== Columna venta_total creada ===")
    print(df[["producto", "precio", "cantidad", "venta_total"]])
    print()

    # Transformacion 9: Crear segmento de precio con pd.cut
    # Fue necesaria para clasificar productos en rangos de precio: bajo, medio, alto
    bins_precio = [0, 1000, 5000, float("inf")]
    etiquetas_precio = ["bajo", "medio", "alto"]
    df["segmento_precio"] = pd.cut(df["precio"], bins=bins_precio, labels=etiquetas_precio)
    print("=== Segmento de precio creado ===")
    print(df[["producto", "precio", "segmento_precio"]])
    print()

    # Transformacion 10: Crear segmento de edad con pd.cut
    # Fue necesaria para clasificar clientes por rango etario
    bins_edad = [0, 25, 35, 50]
    etiquetas_edad = ["joven", "adulto", "maduro"]
    df["segmento_edad"] = pd.cut(df["edad"], bins=bins_edad, labels=etiquetas_edad)
    print("=== Segmento de edad creado ===")
    print(df[["cliente", "edad", "segmento_edad"]])
    print()

    # Guardar el resultado en ventas_procesadas.csv
    df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")
    df.to_csv("../csv/ventas_procesadas.csv", index=False)
    print("=== Archivo guardado como ../csv/ventas_procesadas.csv ===")
    print()
    print("=== DataFrame final ===")
    print(df)

    return df


if __name__ == "__main__":
    df = transformar_datos("../csv/ventas.csv")