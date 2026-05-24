import pandas as pd


def cargar_datos(ruta_csv):
    # Cargar el archivo procesado del Problema 1
    df = pd.read_csv(ruta_csv)
    return df


def tabla_pivot_ciudad_categoria(df):
    # Tabla pivot: total de ventas por ciudad (filas) y categoria (columnas)
    # Permite comparar visualmente que categoria vende mas en cada ciudad
    # Los totales en margenes facilitan la lectura para usuarios no tecnicos
    tabla = pd.pivot_table(
        df,
        values="venta_total",
        index="ciudad",
        columns="categoria",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total",
    )
    print("=== Pivot Table: Ventas por Ciudad y Categoria ===")
    print(tabla)
    print()

    # Informacion que aporta: muestra donde se concentra el volumen de ventas
    # Patron identificable: la categoria con mas ventas por ciudad
    # Estructura adecuada porque los margenes dan el total general


def tabla_pivot_genero_categoria(df):
    # Tabla pivot: promedio de venta por genero y categoria
    # Permite identificar si hay diferencias de gasto entre generos por categoria
    tabla = pd.pivot_table(
        df,
        values="venta_total",
        index="genero",
        columns="categoria",
        aggfunc="mean",
        fill_value=0,
        margins=True,
        margins_name="Promedio",
    )
    print("=== Pivot Table: Promedio de Venta por Genero y Categoria ===")
    print(tabla)
    print()

    # Informacion que aporta: perfil de gasto por genero en cada categoria
    # Patron identificable: que genero gasta mas en tecnologia vs ropa vs hogar
    # Estructura adecuada porque compara promedios entre grupos


def tabla_crosstab_frecuencia(df):
    # Crosstab: frecuencia de transacciones por ciudad y segmento de edad
    # Muestra cuantas transacciones hace cada segmento de edad por ciudad
    # normalize=True convierte a proporciones para ver distribucion relativa
    tabla = pd.crosstab(
        index=df["ciudad"],
        columns=df["segmento_edad"],
        margins=True,
        margins_name="Total",
    )
    print("=== Crosstab: Frecuencia de Transacciones por Ciudad y Edad ===")
    print(tabla)
    print()

    # Informacion que aporta: donde se concentra cada grupo de edad
    # Patron identificable: ciudades preferidas por cada segmento de edad
    # Estructura adecuada porque crosstab es ideal para conteos y proporciones


def tabla_crosstab_proporcion(df):
    # Crosstab con proporcion: distribucion porcentual de categorias por ciudad
    # normalize="index" para que cada fila sume 100%
    tabla = pd.crosstab(
        index=df["ciudad"],
        columns=df["categoria"],
        normalize="index",
    ) * 100
    print("=== Crosstab: Proporcion de Categorias por Ciudad (%) ===")
    print(tabla.round(1))
    print()

    # Informacion que aporta: composicion porcentual de categorias en cada ciudad
    # Patron identificable: ciudades donde domina cierta categoria
    # Estructura adecuada porque porcentajes son mas faciles de interpretar


def resumen_ejecutivo(df):
    # Resumen ejecutivo general con metricas clave
    # Tabla simple que usuarios no tecnicos pueden leer facilmente
    resumen = pd.DataFrame({
        "Metrica": [
            "Total de ventas ($)",
            "Promedio por venta ($)",
            "Venta mas alta ($)",
            "Venta mas baja ($)",
            "Total de transacciones",
            "Total de productos vendidos",
            "Ciudad con mas ventas",
            "Categoria con mas ventas",
        ],
        "Valor": [
            df["venta_total"].sum(),
            round(df["venta_total"].mean(), 2),
            df["venta_total"].max(),
            df["venta_total"].min(),
            df["id_venta"].count(),
            df["cantidad"].sum(),
            df.groupby("ciudad")["venta_total"].sum().idxmax(),
            df.groupby("categoria")["venta_total"].sum().idxmax(),
        ],
    })
    print("=== Resumen Ejecutivo ===")
    print(resumen)
    print()

    # Informacion que aporta: vista rapida de los indicadores mas importantes
    # Patron identificable: la ciudad y categoria dominante
    # Estructura adecuada porque es una tabla simple de 2 columnas facil de leer


if __name__ == "__main__":
    df = cargar_datos("../csv/ventas_procesadas.csv")

    tabla_pivot_ciudad_categoria(df)
    print("=" * 60)

    tabla_pivot_genero_categoria(df)
    print("=" * 60)

    tabla_crosstab_frecuencia(df)
    print("=" * 60)

    tabla_crosstab_proporcion(df)
    print("=" * 60)

    resumen_ejecutivo(df)