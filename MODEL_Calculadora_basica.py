

from tkinter import *

#Funcion para evaluar los resultados de las operaciones
def Evaluar_resultado (operacion):
    """Esta función se utiliza para devolver el resultado de la operación dentro de la calculadora."""
    resultado = str(eval(operacion))
    return resultado