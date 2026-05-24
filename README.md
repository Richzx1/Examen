# Examen - Unidad 3: Programacion para la Extraccion de Datos

**Alumno:** Politron Avila Gerson Ricardo

**Facultad:** FCA
**Materia:** Programacion para la Extraccion de Datos
**Unidad:** Unidad 3
**Tipo:** Parcial
**Catedratico:** Flores Parra Josue Miguel
**Periodo:** Enero - Mayo 2026
**Fecha:** 26/Mayo/2026

---

## Problema 1 - Transformacion de Datos (20%)

Desarrolle una funcion que reciba como parametro la ruta del archivo `ventas.csv`.

La empresa desea preparar la informacion para futuros analisis administrativos y comerciales. El dataset contiene informacion relacionada con clientes, productos, ciudades, categorias, cantidades y precios.

La funcion debera realizar las transformaciones necesarias para mejorar la interpretacion y organizacion de los datos. Ademas, deberan generarse nuevas estructuras o clasificaciones que permitan enriquecer el analisis posterior.

En comentarios explique:
- que transformaciones realizo
- por que fueron necesarias

Finalmente, guardar el resultado en un archivo llamado: `ventas_procesadas.csv`

---

## Problema 2 - Agrupamiento y Segmentacion (20%)

Desarrolle una funcion que utilice la informacion del archivo `ventas_procesadas.csv`. La gerencia comercial desea identificar patrones relacionados con:
- comportamiento de ventas
- ciudades con mayor actividad
- categorias mas relevantes
- perfiles de clientes

El equipo debera aplicar tecnicas de agrupamiento y segmentacion para construir diferentes analisis que permitan responder estas necesidades.

Ademas, deberan generarse al menos:
- un analisis comparativo
- una segmentacion de clientes o ventas
- metricas resumidas relevantes

En comentarios justifique:
- criterios utilizados
- tecnicas seleccionadas
- interpretacion de resultados

---

## Problema 3 - Tablas de Resumen (20%)

Desarrolle una funcion que genere estructuras resumidas a partir del dataset procesado.

La direccion general necesita reportes ejecutivos que permitan:
- comparar categorias
- analizar ciudades
- identificar relaciones entre variables
- detectar patrones generales de comportamiento

El equipo debera construir diferentes tablas de resumen orientadas al analisis ejecutivo. Los reportes deberan facilitar la lectura e interpretacion de la informacion para usuarios no tecnicos.

En comentarios explique:
- que informacion aporta cada resumen
- que patrones pueden identificarse
- por que la estructura elegida resulta adecuada

---

## Problema 4 - Busquedas Dinamicas (20%)

Desarrolle una funcion que permita realizar busquedas dinamicas sobre el dataset.

El departamento de auditoria solicita la capacidad de localizar rapidamente registros especificos relacionados con:
- rangos de edad
- ciudades
- categorias
- productos
- patrones textuales
- combinaciones de multiples condiciones

El equipo debera implementar distintas estrategias de busqueda y filtrado que permitan responder diferentes escenarios de consulta.

En comentarios explique:
- que tecnicas fueron utilizadas
- ventajas de cada enfoque
- diferencias entre los metodos implementados

---

## Problema 5 - Indices y Seleccion Avanzada (20%)

Desarrolle una funcion que reorganice el dataset para facilitar consultas analiticas y acceso eficiente a la informacion.

La empresa desea evaluar diferentes mecanismos de acceso a registros utilizando indices y seleccion avanzada de datos.

El equipo debera implementar distintos esquemas de indexacion y demostrar como estos facilitan:
- consultas especificas
- seleccion de subconjuntos
- acceso por etiquetas
- acceso posicional
- reorganizacion de estructuras

En comentarios explique:
- ventajas observadas
- diferencias entre metodos de acceso
- casos donde cada tecnica resulta mas util

---

## Archivos del Proyecto

| Archivo | Descripcion |
|---------|-------------|
| `transformacion_datos.py` | Problema 1 - Transformacion de datos |
| `agrupamiento_segmentacion.py` | Problema 2 - Agrupamiento y segmentacion |
| `tablas_resumen.py` | Problema 3 - Tablas de resumen |
| `tecnicas_busqueda.py` | Problema 4 - Busquedas dinamicas |
| `indices_pandas.py` | Problema 5 - Indices y seleccion avanzada |
| `mysql_pandas.py` | Conexion MySQL con Pandas |