from tkinter import *
import VIEW_Calculadora_basica as view
import MODEL_Calculadora_basica as model

#Funciones para modificar la vista
#Variables que utilizan las funciones
Historial = [] # Historial es una lista que almacena tuplas con los valores (operacion:total) utilizada en historial
show_ex = "" #Viene a ser la variable que contiene la operación de la calculadora

#Escribir en la consola
def go_to_console (caracter): 
    """La función go_to_console hace que cualquier carácter que se requiera vaya a la consola."""
    global show_ex

    # Aca implemento un "control" cuando ocurre una operacion del tipo "x(x)"
    # Cuando el ultimo dígito de la operación sea un dígito y el carácter que quiera escribir sea "(" se va a colocar un "*"
    # para indicar que ocurre una multiplicación, en la primera parte se coloca show_ex para que funcionen los decimales 
    if show_ex and show_ex[-1].isdigit() and caracter == "(":
        show_ex = show_ex + "*"
    
    # Solo cuando ocurra un evento como ")(" se agregara un "*" entre los dos,
    # caracter se utiliza para que cuando ingrese un ")" y previamente este un
    # ")" no se agrege un signo de multiplicación
    if show_ex and show_ex[-1] == ")" and caracter == "(":
        show_ex = show_ex + "*"

    show_ex = show_ex + str (caracter)
    view.show_in_label.set (show_ex)

#Funcion de igual
def igual ():
    """La función igual devuelve el resultado de la operación actual."""
    global show_ex
    
    try:
        Operacion = show_ex # Esta variable recupera la operación original del resultado para el historial
        total = model.Evaluar_resultado (operacion= show_ex)
        view.show_in_label.set (total)
        show_ex = total
        
        # Cuando el total sea igual a "..." arroja Ellipsis cuando ese evento ocurra 
        # llevará a un error de sintaxis
        if Operacion == "...":
            raise SyntaxError
        
        # Aqui se actualiza el historial desde igual para que el historial no almacene datos erroneos y evitar errores
        historial (Operacion, total)

    except ZeroDivisionError:
       view.show_in_label.set ("Error aritmetico")
       show_ex = ""
    except SyntaxError:
        view.show_in_label.set ("Error de sintaxis")
        show_ex = ""
    
#Limpiar la consola
def limpiar ():
    """Elimina el número que se encuentra actualmente en la consola."""
    global show_ex

    show_ex = ""
    view.show_in_label.set ("")

#Borrar un solo caracter
def delete ():
    """La función delete elimina el último carácter del número que este escribiendo el usuario."""    
    global show_ex

    show_ex = show_ex [:-1]
    view.show_in_label.set (show_ex)

#Actualizar los slots del historial a sus valores verdaderos
def actualizar_historial ():
    """La función "actualizar_historial" establece nuevos valores después de borrar """

    # Aqui se modifica el texto que esta en cada opcion del historial
    # Ejemplo del funcionamiento: "Historial [0][0]"
    # En este caso se accede a la tupla con indice 0 y al elemento con indice 0 de dicha tupla
    # lo que corresponderia a la primera tupla y su primer elemento
    valor_predeterminado = "-Vacio-"
    try:
        # Se establece el valor de las stringvar en 
        view.Slot1_str.set (valor_predeterminado); view.Slot2_str.set (valor_predeterminado); view.Slot3_str.set (valor_predeterminado)
        view.Slot4_str.set (valor_predeterminado); view.Slot5_str.set (valor_predeterminado); view.Slot6_str.set (valor_predeterminado)

        view.Slot1_str.set (f"Operación: {Historial [0][0]} = {Historial [0][1]}")
        view.Slot2_str.set (f"Operación: {Historial [1][0]} = {Historial [1][1]}")
        view.Slot3_str.set (f"Operación: {Historial [2][0]} = {Historial [2][1]}")
        view.Slot4_str.set (f"Operación: {Historial [3][0]} = {Historial [3][1]}")
        view.Slot5_str.set (f"Operación: {Historial [4][0]} = {Historial [4][1]}")
        view.Slot6_str.set (f"Operación: {Historial [5][0]} = {Historial [5][1]}")
    except IndexError:
        pass

#Funcion del historial (se utiliza una lista para almacenar las operaciones)
def historial (Operacion, total):
    """La función historial almacena los datos de las operaciones anteriores para que las vea el usuario"""
    global Historial

    #Aqui se guardan las operaciones anteriores en una tupla dentro de la lista "Historial"
    Historial.insert (0, (Operacion, total))
    actualizar_historial ()

#Funcion para los botones del historial
def reemplazar (rem):
    """La función reemplazar cambiará la operación del historial a la consola.
    \n El argumento "rem" indica cual de los valores que se encuentra en los slots va a reemplazarse en la consola."""
    global show_ex
    try:
        # Aqui lo que ocurre es que dependiendo del valor que tenga rem, va a buscarse la tupla correspondiente
        # restandose el valor -1, en este caso si rem = 1, va a buscarse la primera tupla y su primer elemento 
        # que es la operacion anterior se va a reemplazar dentro de la consola, además de que se evita poner un
        # monton de "elif" con distintas condiciones

        show_ex = Historial [rem-1][0]
        view.show_in_label.set (show_ex)

    except IndexError:
        pass
    
#Funcion de ans
def ANS ():
    """La función ANS devuelve el último resultado de la operación anterior."""
    try:
        go_to_console (Historial [0][1])
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
            connect.guardar_operacion (inv.True_User, f"{Historial [0][0]}")
        elif operacion == 2:
            connect.guardar_operacion (inv.True_User, f"{Historial [1][0]}")
        elif operacion == 3:
            connect.guardar_operacion (inv.True_User, f"{Historial [2][0]}")
        elif operacion == 4:
            connect.guardar_operacion (inv.True_User, f"{Historial [3][0]}")
        elif operacion == 5:
            connect.guardar_operacion (inv.True_User, f"{Historial [4][0]}")
        elif operacion == 6:
            connect.guardar_operacion (inv.True_User, f"{Historial [5][0]}")
    except IndexError:
        pass

# Funciones de guardado
def acciones_del_historial (indice, invitado):
    """La función "acciones_del_historial" desplega un menu que permite eliminar opciones del historial o guardarlas en la base de datos."""
    from VIEW_Calculadora_basica import operaciones_incloud, operaciones
    
    global indice_a_eliminar
    indice_a_eliminar = indice
    
    if invitado == False:
        Menu_de_acciones = Menu (view.Memory_frame, tearoff= 0)
        Menu_de_acciones.add_command (label= "Guardar en la nube", command= lambda: (guardar_indices (indice), operaciones.destroy(), operaciones_incloud ()))
        Menu_de_acciones.add_separator ()
        Menu_de_acciones.add_command (label= "Eliminar del historial", command= lambda: (eliminar_indices (), actualizar_historial ()))
    
        Menu_de_acciones.post (view.raiz.winfo_pointerx (), view.raiz.winfo_pointery ())
    
    else:
        Menu_de_acciones = Menu (view.Memory_frame, tearoff= 0)
        Menu_de_acciones.add_command (label= "Guardar en la nube", state= "disabled")
        Menu_de_acciones.add_separator ()
        Menu_de_acciones.add_command (label= "Eliminar del historial", command= lambda: (eliminar_indices (), actualizar_historial ()))
    
        Menu_de_acciones.post (view.raiz.winfo_pointerx (), view.raiz.winfo_pointery ()) 

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
    global show_ex
    try:
        show_ex =  operaciones_guardadas [rem-1]
        view.show_in_label.set (show_ex)

    except IndexError:
        pass

# Funciones de guardado
def acciones_del_historial_cloud (indice, usuario):
    """La función "acciones_del_historial" desplega un menu que permite eliminar opciones del historial o guardarlas en la base de datos."""
    
    from MODEL_firebase import delete_operaciones

    # Menu de opciones para la nube
    Menu_de_acciones = Menu (view.Memory_frame, tearoff= 0)
    Menu_de_acciones.add_command (label= "Eliminar de la base de datos", command= lambda: (delete_operaciones (usuario, indice)))
    
    Menu_de_acciones.post (view.raiz.winfo_pointerx (), view.raiz.winfo_pointery ())