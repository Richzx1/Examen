import pandas as pd


def cargar_datos(ruta_csv):
    # Cargar el archivo procesado del Problema 1
    df = pd.read_csv(ruta_csv)
    return df


def indices_numericos_iloc(df):
    # iloc: acceso posicional por numeros de fila y columna
    # Ventaja: rapido y directo, no depende de etiquetas
    # Caso util: cuando se sabe la posicion exacta y no importa el nombre de la columna

    # Seleccionar las primeras 5 filas y columnas 0 a 3
    print("=== iloc: Primeras 5 filas, columnas 0 a 3 ===")
    print(df.iloc[0:5, 0:4])
    print()

    # Seleccionar filas especificas con todas las columnas
    print("=== iloc: Filas 2, 5, 10 ===")
    print(df.iloc[[2, 5, 10]])
    print()

    # Seleccionar solo columnas de precio y venta_total (columnas 9 y 11)
    print("=== iloc: Filas 0 a 9, columnas precio y venta_total ===")
    print(df.iloc[0:10, [8, 10]])
    print()

    # Modificar un valor usando iloc (cambio temporal para demostracion)
    df_temp = df.copy()
    df_temp.iloc[0, 8] = 99999
    print("=== iloc: Primer precio modificado ===")
    print(df_temp.iloc[0:3, [1, 8]])
    print()


def indices_etiquetas_loc(df):
    # loc: acceso por etiquetas (nombres de filas y columnas)
    # Ventaja: mas legible y seguro, se usa el nombre de la columna
    # Caso util: cuando se necesita filtrar por nombre de columna o condiciones

    # Seleccionar columnas especificas por nombre
    print("=== loc: Columnas cliente, ciudad, venta_total ===")
    print(df.loc[:, ["cliente", "ciudad", "venta_total"]])
    print()

    # Filtrar filas por condicion usando loc
    print("=== loc: Ventas en CDMX ===")
    print(df.loc[df["ciudad"] == "CDMX", ["cliente", "producto", "precio", "venta_total"]])
    print()

    # Modificar valor con loc (cambio temporal para demostracion)
    df_temp = df.copy()
    df_temp["precio"] = df_temp["precio"].astype(float)
    df_temp.loc[df_temp["ciudad"] == "Monterrey", "precio"] = df_temp.loc[df_temp["ciudad"] == "Monterrey", "precio"] * 1.05
    print("=== loc: Precios en Monterrey aumentados 5% ===")
    print(df_temp.loc[df_temp["ciudad"] == "Monterrey", ["cliente", "producto", "precio"]])
    print()


def reorganizar_indices(df):
    # set_index: cambiar el indice del DataFrame a una columna existente
    # Ventaja: permite busquedas rapidas por el valor del indice
    # Caso util: cuando se busca frecuentemente por id_venta, ciudad, etc.

    # Usar id_venta como indice
    df_index = df.copy()
    df_index.set_index("id_venta", inplace=True)
    print("=== set_index: id_venta como indice ===")
    print(df_index.head())
    print()

    # Busqueda rapida por indice usando loc
    print("=== Busqueda por id_venta ===")
    print(df_index.loc[[1, 5, 10]])
    print()

    # Usar ciudad como indice
    df_ciudad = df.copy()
    df_ciudad.set_index("ciudad", inplace=True)
    print("=== set_index: ciudad como indice ===")
    print(df_ciudad.head())
    print()

    # Buscar todas las ventas en Monterrey
    print("=== Ventas en Monterrey usando indice ===")
    print(df_ciudad.loc["Monterrey"])
    print()

    # reset_index: devolver el indice a columna y usar indice numerico
    df_ciudad.reset_index(inplace=True)
    print("=== reset_index: indice restaurado ===")
    print(df_ciudad.head())
    print()


def seleccion_avanzada(df):
    # Seleccion de subconjuntos con condiciones combinadas
    # Ventaja: permite consultas especificas y complejas

    # Subconjunto: solo columnas relevantes para analisis de ventas
    subconjunto = df[["id_venta", "cliente", "ciudad", "categoria", "producto", "venta_total"]]
    print("=== Subconjunto: columnas relevantes ===")
    print(subconjunto.head(10))
    print()

    # Subconjunto filtrado: ventas de Tecnologia en Monterrey
    filtro = df[(df["categoria"] == "Tecnologia") & (df["ciudad"] == "Monterrey")]
    print("=== Subconjunto filtrado: Tecnologia en Monterrey ===")
    print(filtro[["cliente", "producto", "venta_total"]])
    print()

    # Seleccion con loc y condicion multiple
    resultado = df.loc[
        (df["segmento_precio"] == "alto") & (df["genero"] == "F"),
        ["cliente", "producto", "precio", "segmento_precio"],
    ]
    print("=== loc: Productos de precio alto comprados por mujeres ===")
    print(resultado)
    print()


def estadisticas_describe(df):
    # describe(): resumen estadistico que facilita consultas rapidas
    # Ventaja: da un panorama general en una sola linea
    # Se puede acceder a estadisticas especificas con loc o iloc

    stats = df[["edad", "cantidad", "precio", "venta_total"]].describe()
    print("=== Estadisticas descriptivas ===")
    print(stats)
    print()

    # Acceder a estadisticas especificas con loc
    print("=== Estadisticas especificas (mean, max, min) ===")
    print(stats.loc[["mean", "max", "min"]])
    print()

    # Acceder con iloc (posicion: 1=mean, 3=min, 7=max)
    print("=== Estadisticas especificas con iloc ===")
    print(stats.iloc[[1, 3, 7]])
    print()


if __name__ == "__main__":
    df = cargar_datos("../csv/ventas_procesadas.csv")

    indices_numericos_iloc(df)
    print("=" * 60)

    indices_etiquetas_loc(df)
    print("=" * 60)

    reorganizar_indices(df)
    print("=" * 60)

    seleccion_avanzada(df)
    print("=" * 60)

    estadisticas_describe(df)