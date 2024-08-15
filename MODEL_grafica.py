import re
import tkinter as tk

def correc_ecuacion (ecuacion):
    #Reemplazos para que las funciones trigonometricas sean accesibles al eval()
    ecuacion = re.sub(r'sin\(', '(<1>>', ecuacion)
    ecuacion = re.sub(r'cos\(', '(<2>>', ecuacion)
    ecuacion = re.sub(r'tan\(', '(<3>>', ecuacion)
    ecuacion = re.sub(r'csc\(', '(<4-4>>', ecuacion)
    ecuacion = re.sub(r'sec\(', '(<5-5>>', ecuacion)
    ecuacion = re.sub(r'ctn\(', '(<6-6>>', ecuacion)

    ecuacion = re.sub(r'[a-zA-Z]', r'x', ecuacion)   
    
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
    ecuacion = re.sub(r'\(<1>>', 'np.sin(', ecuacion)
    ecuacion = re.sub(r'\(<2>>', 'np.cos(', ecuacion)
    ecuacion = re.sub(r'\(<3>>', 'np.tan(', ecuacion)
    ecuacion = re.sub(r'\(<4-4>>', 'np.arcsin(', ecuacion)
    ecuacion = re.sub(r'\(<5-5>>', 'np.arccos(', ecuacion)
    ecuacion = re.sub(r'\(<6-6>>', 'np.arctan(', ecuacion)   
    
    return ecuacion

def correc_historial(ecuacion):
    ecuacion = re.sub(r'np.sin\(','sin(', ecuacion)
    ecuacion = re.sub(r'np.cos\(','cos(', ecuacion)
    ecuacion = re.sub(r'np.tan\(','tan(', ecuacion)
    ecuacion = re.sub(r'np.arcsin\(','csc(', ecuacion)
    ecuacion = re.sub(r'np.arccos\(','sec(', ecuacion)
    ecuacion = re.sub(r'np.arctan\(','ctn(', ecuacion) 

    return ecuacion

#Variables que utilizan las funciones
Historial = [] # Historial es una lista que almacena las funciones que ha ingresado el usuario

def actualizar_historial ():
    """La función "actualizar_historial" establece nuevos valores después de borrar alguna de sus opciones"""

    from VIEW_cal_grafica import Slot1_str, Slot2_str, Slot3_str, Slot4_str, Slot5_str, Slot6_str

    # Aqui se modifica el texto que esta en cada opcion del historial
    # Ejemplo del funcionamiento: "Historial [0]"
    # En este caso se accede a elemento de indice 0 
    # lo que corresponderia a la primera tupla y su primer elemento
    valor_predeterminado = "-Vacio-"
    try:
        # Se establece el valor de las stringvar en su valor predeterminado
        Slot1_str.set (valor_predeterminado); Slot2_str.set (valor_predeterminado); Slot3_str.set (valor_predeterminado)
        Slot4_str.set (valor_predeterminado); Slot5_str.set (valor_predeterminado); Slot6_str.set (valor_predeterminado)

        Slot1_str.set (f"Función: {Historial [0]}")
        Slot2_str.set (f"Función: {Historial [1]}")
        Slot3_str.set (f"Función: {Historial [2]}")
        Slot4_str.set (f"Función: {Historial [3]}")
        Slot5_str.set (f"Función: {Historial [4]}")
        Slot6_str.set (f"Función: {Historial [5]}")
    except IndexError:
        pass

#Funcion del historial (se utiliza una lista para almacenar las operaciones)
def historial (funcion):
    """La función historial almacena los datos de las operaciones anteriores para que las vea el usuario"""
    global Historial

    #Aqui se guardan las operaciones anteriores en una tupla dentro de la lista "Historial"
    Funcion_corregida = correc_historial(funcion)
    Historial.insert (0, Funcion_corregida)
    
    actualizar_historial()

#Funcion para los botones del historial
def reemplazar (rem):
    """La función reemplazar cambiará la operación del historial a la consola.
    /n El argumento "rem" indica cual de los valores que se encuentra en los slots va a reemplazarse en la consola."""
    
    from VIEW_cal_grafica import Slot1, Slot2, Slot3, Slot4, Slot4, Slot5, Slot6, Memory_frame, Slot1_str, Slot2_str, Slot3_str, Slot4_str, Slot5_str, Slot6_str, Entrada_funciones
    try:
        # Aqui lo que ocurre es que dependiendo del valor que tenga rem, va a buscarse la tupla correspondiente
        # restandose el valor -1, en este caso si rem = 1, va a buscarse la primera tupla y su primer elemento 
        # que es la operacion anterior se va a reemplazar dentro de la consola, además de que se evita poner un
        # monton de "elif" con distintas condiciones

        Funcion_a_reemplazar = Historial [rem-1]
        
        Entrada_funciones.delete (0, tk.END)
        Entrada_funciones.insert (0, Funcion_a_reemplazar)

    except IndexError:
        pass

#Funcion para eliminar opciones del historial
def eliminar_indices ():
    """Elimina opciones del historial."""
    try:
        #Remueve la opcion del historial que quiera 
        Historial.pop (indice_a_eliminar-1)
    except IndexError:
        pass

#Guardar operaciones de la calculadora
def guardar_indices (operacion):
    """La función "guardar_indices" almacena las operaciones con sus respectivos resultados en la base de datos."""
    import MODEL_firebase as connect
    import firebase_controller as inv

    # Guardadp de operaciones
    try:
        if operacion == 1:
            connect.guardar_funcion_grafica (inv.True_User, f"{Historial [0]}")
        elif operacion == 2:
            connect.guardar_funcion_grafica (inv.True_User, f"{Historial [1]}")
        elif operacion == 3:
            connect.guardar_funcion_grafica (inv.True_User, f"{Historial [2]}")
        elif operacion == 4:
            connect.guardar_funcion_grafica (inv.True_User, f"{Historial [3]}")
        elif operacion == 5:
            connect.guardar_funcion_grafica (inv.True_User, f"{Historial [4]}")
        elif operacion == 6:
            connect.guardar_funcion_grafica (inv.True_User, f"{Historial [5]}")
    except IndexError:
        pass

# Funciones de guardado
def acciones_del_historial (indice, invitado):
    """La función "acciones_del_historial" desplega un menu que permite eliminar opciones del historial o guardarlas en la base de datos."""
    
    from VIEW_cal_grafica import Memory_frame, raiz, operaciones, funciones_incloud

    global indice_a_eliminar
    indice_a_eliminar = indice
    
    if invitado == False:
        Menu_de_acciones = tk.Menu (Memory_frame, tearoff= 0)
        Menu_de_acciones.add_command (label= "Guardar en la nube", command= lambda: (guardar_indices (indice), operaciones.destroy (), funciones_incloud ()))
        Menu_de_acciones.add_separator ()
        Menu_de_acciones.add_command (label= "Eliminar del historial", command= lambda: (eliminar_indices (), actualizar_historial ()))
    
        Menu_de_acciones.post (raiz.winfo_pointerx (), raiz.winfo_pointery ())
    
    else:
        Menu_de_acciones = tk.Menu (Memory_frame, tearoff= 0)
        Menu_de_acciones.add_command (label= "Guardar en la nube", state= "disabled")
        Menu_de_acciones.add_separator ()
        Menu_de_acciones.add_command (label= "Eliminar del historial", command= lambda: (eliminar_indices (), actualizar_historial ()))
    
        Menu_de_acciones.post (raiz.winfo_pointerx (), raiz.winfo_pointery ()) 

# Función para borrar todo el historial
def clear_all ():

    """La función "clear_all" elimina todo el contenido del historial."""
    
    # El metodo ".Clear ()" vacia la lista historial
    Historial.clear ()
    actualizar_historial ()

#Funcion para los botones del historial para la database
def reemplazar_en_la_nube (rem, operaciones_guardadas):
    """La función reemplazar cambiará la operación del historial de la nube a la consola.
    \n El argumento "rem" indica cual de los valores que se encuentra en los slots va a reemplazarse en la consola."""

    try:
        from VIEW_cal_grafica import Entrada_funciones
        contenido_database =  operaciones_guardadas [rem-1]

        Entrada_funciones.delete (0, tk.END)
        Entrada_funciones.insert (0, contenido_database)

    except IndexError:
        pass