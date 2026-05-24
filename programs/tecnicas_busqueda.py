import pandas as pd


def cargar_datos(ruta_csv):
    # Cargar el archivo procesado del Problema 1
    df = pd.read_csv(ruta_csv)
    return df


def busqueda_booleana(df):
    # Tecnica: filtrado booleano con condiciones
    # Ventaja: sintaxis simple y directa, facil de leer
    # Permite combinar condiciones con & (AND) y | (OR)

    # Ventas mayores a 5000
    filtro_precio = df[df["venta_total"] > 5000]
    print("=== Busqueda: Ventas mayores a $5,000 ===")
    print(filtro_precio[["cliente", "producto", "venta_total"]])
    print()

    # Clientes jovenes (edad <= 25) que compraron tecnologia
    filtro_joven_tec = df[(df["edad"] <= 25) & (df["categoria"] == "Tecnologia")]
    print("=== Busqueda: Jovenes que compraron Tecnologia ===")
    print(filtro_joven_tec[["cliente", "edad", "categoria", "producto"]])
    print()

    # Ventas en Monterrey o CDMX con precio mayor a 5000
    filtro_ciudad_precio = df[(df["ciudad"].isin(["Monterrey", "CDMX"])) & (df["precio"] > 5000)]
    print("=== Busqueda: Monterrey o CDMX con precio > $5,000 ===")
    print(filtro_ciudad_precio[["ciudad", "producto", "precio"]])
    print()


def busqueda_isin(df):
    # Tecnica: isin() para filtrar por multiples valores en una columna
    # Ventaja: mas limpio que encadenar multiples == con |
    # Ideal cuando se tienen varios valores posibles para una misma columna

    # Ventas en categorias especificas
    filtro_cat = df[df["categoria"].isin(["Tecnologia", "Hogar"])]
    print("=== Busqueda isin: Ventas en Tecnologia u Hogar ===")
    print(filtro_cat[["cliente", "categoria", "producto", "venta_total"]])
    print()

    # Clientes en ciertas ciudades
    filtro_ciudad = df[df["ciudad"].isin(["Monterrey", "CDMX", "Guadalajara"])]
    print("=== Busqueda isin: Ventas en Monterrey, CDMX, Guadalajara ===")
    print(filtro_ciudad[["cliente", "ciudad", "producto"]])
    print()


def busqueda_texto(df):
    # Tecnica: str.contains() para buscar patrones de texto
    # Ventaja: permite busquedas parciales sin conocer el nombre exacto
    # Util para auditoria cuando se busca por descripcion parcial

    # Productos que contengan "Laptop"
    filtro_laptop = df[df["producto"].str.contains("Laptop", case=False)]
    print("=== Busqueda textual: Productos con 'Laptop' ===")
    print(filtro_laptop[["producto", "categoria", "precio", "venta_total"]])
    print()

    # Productos que contengan "S" (Playera Sport, Sudadera, Smartwatch, Sofa, etc.)
    filtro_s = df[df["producto"].str.contains("^S", case=False)]
    print("=== Busqueda textual: Productos que empiezan con 'S' ===")
    print(filtro_s[["producto", "categoria", "precio"]])
    print()


def busqueda_query(df):
    # Tecnica: df.query() para busqueda con sintaxis tipo SQL
    # Ventaja: sintaxis mas legible para consultas complejas
    # Diferencia con booleana: permite usar variables externas con @ y es mas concisa

    # Ventas con precio mayor a 3000
    precio_min = 3000
    resultado = df.query("precio > @precio_min")
    print("=== Busqueda query: Precio mayor a $3,000 ===")
    print(resultado[["cliente", "producto", "precio"]])
    print()

    # Clientes jovenes con compras de tecnologia
    resultado2 = df.query("edad <= 25 and categoria == 'Tecnologia'")
    print("=== Busqueda query: Jovenes comprando Tecnologia ===")
    print(resultado2[["cliente", "edad", "producto", "precio"]])
    print()

    # Busqueda con isin dentro de query
    resultado3 = df.query("ciudad.isin(['Monterrey', 'CDMX'])")
    print("=== Busqueda query: Ventas en Monterrey o CDMX ===")
    print(resultado3[["cliente", "ciudad", "producto"]])
    print()


def busqueda_valores_unicos(df):
    # Tecnica: unique() y value_counts() para explorar distribucion de datos
    # Ventaja: rapido panorama de que valores existen y cuantas veces aparecen
    # Util para auditoria: detectar inconsistencias o valores atipicos

    print("=== Valores unicos por columna ===")
    print(f"Ciudades: {df['ciudad'].unique()}")
    print(f"Categorias: {df['categoria'].unique()}")
    print(f"Generos: {df['genero'].unique()}")
    print(f"Segmentos de precio: {df['segmento_precio'].unique()}")
    print()

    print("=== Conteo de valores: categoria ===")
    print(df["categoria"].value_counts())
    print()
    print("=== Conteo de valores: ciudad ===")
    print(df["ciudad"].value_counts())
    print()


def busqueda_tops(df):
    # Tecnica: nlargest() y nsmallest() para encontrar extremos rapidamente
    # Ventaja: mas eficiente que ordenar todo el dataframe cuando solo necesitas los N primeros
    # Diferencia con sort_values: no ordena todo el dataframe, solo extrae lo solicitado

    # Top 5 ventas mas altas
    top5 = df.nlargest(5, columns="venta_total")
    print("=== Top 5 ventas mas altas ===")
    print(top5[["cliente", "producto", "venta_total", "ciudad"]])
    print()

    # Top 5 ventas mas bajas
    bottom5 = df.nsmallest(5, columns="venta_total")
    print("=== Top 5 ventas mas bajas ===")
    print(bottom5[["cliente", "producto", "venta_total", "ciudad"]])
    print()

    # Top 3 clientes que mas gastaron
    top_clientes = df.groupby("cliente")["venta_total"].sum().nlargest(3)
    print("=== Top 3 clientes con mayor gasto ===")
    print(top_clientes)
    print()


if __name__ == "__main__":
    df = cargar_datos("../csv/ventas_procesadas.csv")

    busqueda_booleana(df)
    print("=" * 60)

    busqueda_isin(df)
    print("=" * 60)

    busqueda_texto(df)
    print("=" * 60)

    busqueda_query(df)
    print("=" * 60)

    busqueda_valores_unicos(df)
    print("=" * 60)

    busqueda_tops(df)