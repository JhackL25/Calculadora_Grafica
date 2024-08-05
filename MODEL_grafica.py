import re
import numpy as np
def correc_ecuacion(ecuacion):
    #Reemplazos para que las funciones trigonometricas sean accesibles al eval()
    ecuacion = re.sub(r'sin\(', '(<S>>', ecuacion)
    ecuacion = re.sub(r'cos\(', '(<C>>', ecuacion)
    ecuacion = re.sub(r'tan\(', '(<T>>', ecuacion)
    ecuacion = re.sub(r'csc\(', '(<C-s>>', ecuacion)
    ecuacion = re.sub(r'sec\(', '(<S-c>>', ecuacion)
    ecuacion = re.sub(r'ctn\(', '(<C-t>>', ecuacion)
    
    #cambios necesarios para operar eval()
    ecuacion = re.sub(r'([a-zA-Z])(\()', r'\1*\2', ecuacion)    # Variable y paréntesis abierto
    ecuacion = re.sub(r'(\))([a-zA-Z0-9])', r'\1*\2', ecuacion)  # Paréntesis cerrado y variable o número
    ecuacion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', ecuacion)      # Número y variable
    ecuacion = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', ecuacion)      # Variable y número
    ecuacion = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', ecuacion) # Dos variables
    ecuacion = re.sub(r'(\))(\()', r'\1*\2', ecuacion)            # Paréntesis cerrado y abierto
    ecuacion = re.sub(r'(\d)(\()', r'\1*\2', ecuacion)             # Número y paréntesis abierto
    ecuacion = re.sub(r'(\d)(π)', r'\1*\2', ecuacion)              #Numero y Pi
    ecuacion = re.sub(r'(π)(\()', r'\1*\2', ecuacion)              #Pi y parentesis
    ecuacion = re.sub(r'(π)([a-zA-Z])', r'\1*\2', ecuacion)

    #Reestaurar funciones trigonometricas
    ecuacion = re.sub(r'\(<S>>', 'np.sin(', ecuacion)
    ecuacion = re.sub(r'\(<C>>', 'np.cos(', ecuacion)
    ecuacion = re.sub(r'\(<T>>', 'np.tan(', ecuacion)
    ecuacion = re.sub(r'\(<C-s>>', 'np.arcsin(', ecuacion)
    ecuacion = re.sub(r'\(<S-c>>', 'np.arccos(', ecuacion)
    ecuacion = re.sub(r'\(<C-t>>', 'np.arctan(', ecuacion)   
    
    return ecuacion

def correc_historial(Historial):
    Historial = (f"'{Historial}'")
    Historial = Historial.replace('[', '')
    Historial = Historial.replace(']', '')
    Historial = Historial.replace("'", '')   

    print(Historial)
    return Historial
