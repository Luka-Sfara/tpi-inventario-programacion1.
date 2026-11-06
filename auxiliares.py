import os

def limpiar_pantalla(): # limpia la terminal
    os.system("cls" )

def es_duplicados(inventario:list, herramienta:str): # recorre cada diccionario buscando un valor y comparandolo los valores de la clave "herramienta"
    for producto in inventario:
        if producto["herramienta"].lower() == herramienta.lower():
            return True
    return False

def busqueda(inventario: list, herramienta: str): # recorre cada diccionario buscando un valor y devuelve el diccionario donde se encuentre
    for producto in inventario:
        if producto["herramienta"].lower() == herramienta.lower(): # .lower() para que el producto buscando y el de inventario no devuelvan falso si tiene mayusculas
            return producto
    return None

