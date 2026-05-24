import pandas as pd


def cargar_datos(ruta_csv):
    # Cargar el archivo procesado del Problema 1
    df = pd.read_csv(ruta_csv)
    return df


def analisis_comparativo(df):
    # Analisis comparativo: ventas totales por ciudad y categoria
    # Se uso groupby con agg nombrada para obtener metricas claras por ciudad
    # Esto permite identificar ciudades con mayor actividad comercial
    comparativo = df.groupby("ciudad").agg(
        total_ventas=("venta_total", "sum"),
        promedio_ventas=("venta_total", "mean"),
        total_cantidad=("cantidad", "sum"),
        num_transacciones=("id_venta", "count"),
    )
    print("=== Analisis comparativo por ciudad ===")
    print(comparativo)
    print()

    # Comparativo por categoria
    # Permite ver que categoria genera mas ingresos y mas ventas
    comparativo_cat = df.groupby("categoria").agg(
        total_ventas=("venta_total", "sum"),
        promedio_ventas=("venta_total", "mean"),
        total_cantidad=("cantidad", "sum"),
        num_transacciones=("id_venta", "count"),
    )
    print("=== Analisis comparativo por categoria ===")
    print(comparativo_cat)
    print()


def segmentacion_clientes(df):
    # Segmentacion de clientes por edad usando pd.cut
    # Se eligieron rangos basados en el perfil de consumo: joven, adulto, maduro
    # Esto permite identificar perfiles de clientes y su comportamiento de compra
    segmento_edad = df.groupby("segmento_edad", observed=True).agg(
        total_gastado=("venta_total", "sum"),
        promedio_gastado=("venta_total", "mean"),
        num_compras=("id_venta", "count"),
    )
    print("=== Segmentacion de clientes por edad ===")
    print(segmento_edad)
    print()

    # Segmentacion por genero
    # Permite ver diferencias en comportamiento de compra entre generos
    segmento_genero = df.groupby("genero").agg(
        total_gastado=("venta_total", "sum"),
        promedio_gastado=("venta_total", "mean"),
        num_compras=("id_venta", "count"),
    )
    print("=== Segmentacion de clientes por genero ===")
    print(segmento_genero)
    print()

    # Segmentacion por precio usando pd.qcut (cuantiles automaticos)
    # Se uso qcut para dividir en terciles automaticos segun la distribucion real
    df["segmento_ingreso"] = pd.qcut(df["venta_total"], q=3, labels=["bajo", "medio", "alto"])
    segmento_ingreso = df.groupby("segmento_ingreso", observed=True).agg(
        venta_min=("venta_total", "min"),
        venta_max=("venta_total", "max"),
        total_ventas=("venta_total", "sum"),
        num_transacciones=("id_venta", "count"),
    )
    print("=== Segmentacion de ventas por ingreso (qcut) ===")
    print(segmento_ingreso)
    print()


def metricas_resumidas(df):
    # Metricas generales del dataset
    # Se uso describe() para obtener un resumen estadistico completo
    print("=== Metricas resumidas generales ===")
    print(df[["edad", "cantidad", "precio", "venta_total"]].describe())
    print()

    # Metricas por ciudad y categoria combinadas
    # Permite ver el comportamiento de ventas en cada interseccion
    combinado = df.groupby(["ciudad", "categoria"]).agg(
        total_ventas=("venta_total", "sum"),
        promedio_ventas=("venta_total", "mean"),
        num_transacciones=("id_venta", "count"),
    )
    print("=== Metricas combinadas ciudad-categoria ===")
    print(combinado)
    print()


if __name__ == "__main__":
    df = cargar_datos("../csv/ventas_procesadas.csv")

    # Analisis comparativo
    analisis_comparativo(df)
    print("=" * 60)

    # Segmentacion de clientes y ventas
    segmentacion_clientes(df)
    print("=" * 60)

    # Metricas resumidas
    metricas_resumidas(df)