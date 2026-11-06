# Sistema de Control de Inventario - Ferretería

Trabajo Práctico Integrador de **Programación 1**
Tecnicatura Universitaria en Programación - UTN

**Alumno:** Luka Sfara

---

## Enlaces

- 🎥 **Video demostrativo:** [Video presentacion TPI](https://www.youtube.com/watch?v=Q1ZTABVVAzQ)
- 📄 **Informe en PDF:** [Informe.pdf](./Informe.pdf)

---

## Descripción

Programa en Python con menú interactivo para controlar el inventario de una ferretería. Cada operación actualiza el stock en el momento, mientras el programa está en ejecución. Los datos viven en memoria (una lista de diccionarios llamada `inventario`) y **no se guardan al cerrar el programa**.

Cada herramienta se representa con un diccionario:

```python
{"herramienta": "Martillo", "cantidad": 10}
```

## Opciones del menú

| Opción | Función | Qué hace |
|---|---|---|
| 1 | `cargar_herramientas` | Carga varias herramientas con su stock inicial. Si un dato es inválido, lo informa y lo vuelve a pedir. |
| 2 | `mostrar_inventario` | Lista todas las herramientas con su stock. |
| 3 | `consultar_stock` | Muestra el stock de una herramienta buscada por nombre. |
| 4 | `reporte_agotados` | Lista las herramientas con stock igual a 0. |
| 5 | `alta_producto` | Agrega una herramienta nueva al final del inventario. |
| 6 | `actualizar_stock` | Registra una venta (resta) o un ingreso (suma) de unidades. |
| 7 | - | Sale del programa (se resuelve en `main()`). |

## Cómo ejecutarlo

1. Tener Python instalado (desarrollado con Python 3.14.5 en Windows 11).
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

```
python main.py
```

## Estructura del proyecto

```
├── main.py         # Menú principal, bucle y manejo de errores (try/except)
├── opciones.py     # Las 6 funciones de las opciones del menú
├── auxiliares.py   # Funciones de apoyo: limpiar_pantalla, es_duplicados, busqueda
├── Informe.pdf     # Informe de diseño, diagrama de flujo y recursos utilizados
└── README.md
```

El archivo que se ejecuta para iniciar el programa es **`main.py`**.

## Decisiones de diseño

- `inventario` se crea dentro de `main()` y se pasa por parámetro a cada función: no hay variables globales.
- No se usan clases ni otras colecciones: solo la lista `inventario`.
- Los nombres de herramientas se comparan ignorando mayúsculas y espacios en los extremos, pero se guardan como los escribió el usuario.
- **Manejo de errores:** la opción 1 captura los errores dentro de la función y reintenta; en las opciones 3, 5 y 6 el error sale hacia `main()`, que muestra el motivo y vuelve al menú.
- Un dato inválido nunca deja datos a medias: el stock solo se modifica cuando todas las validaciones pasaron.
