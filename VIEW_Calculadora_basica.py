from tkinter import *
import MODEL_Funciones_Calculadora_basica as model
import VIEW_cal_grafica as graf

def calculadora_basica ():
    global show_in_label, Variable_de_control, Slot1, Slot2, Slot3, Slot4, Slot4, Slot5, Slot6, Memory_frame, raiz, Slot1_str, Slot2_str, Slot3_str, Slot4_str, Slot5_str, Slot6_str, Menu_principal

    #Creacion de la ventana
    raiz = Toplevel ()
    raiz.geometry ("600x645")
    raiz.title ("Calculadora basica")
    raiz.resizable (False, False)

    #Menu de opciones para cambiar programas
    Menu_principal = Menu (raiz)
    raiz.config (menu= Menu_principal) #Esto es para que la barra del menu este en la esquina

    #Opciones del menu
    Menu_principal.add_command (label= "Calculadora gráfica", command = lambda: ((raiz.withdraw(), graf.cal_graf_tkinter_vs ())))
    
    #Variable para la consola
    show_in_label = StringVar ()

    #Frame de la consola y el teclado
    Ventana_principal= Frame (raiz, pady= 10, padx= 20)
    Ventana_principal.grid (column= 0, row= 0, rowspan= 2) #Agregue la fila 0

    #Frame del historial
    Memory_frame = Frame (raiz, borderwidth= 1, relief= "solid")
    Memory_frame.grid (column= 1, row= 0)
    #Memory_frame.place (relx= 0.785, rely= 0.02, anchor= "n")

    #Label/titulo para el historial
    Titulo = Label (Memory_frame, text= "Historial", font= ("Consolas", 16))
    Titulo.grid (column= 0, row= 0)

    #Consola (Aquí se muestran los caracteres que utilice la calculadora)
    consola = Label (Ventana_principal, textvariable= show_in_label, font= ("consolas", 18), bg= "white", width= 24, height= 2, borderwidth= 1, relief= "groove")
    consola.grid (row= 0, column= 1, sticky= N+E+S+W)

    #Frame de botones
    win_bt= Frame (Ventana_principal, pady= 10)
    win_bt.grid (row= 1, column= 1)

    # Widgets de la vista, en este caso corresponden al teclado
    # Espacios para las opciones de los slots del historial

    #Variable para el modo invitado
    Variable_de_control = False
    
    # Para el Slot 1 
    Boton_de_opciones = Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: model.acciones_del_historial (1, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=1)

    # Para el Slot 2
    Boton_de_opciones = Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: model.acciones_del_historial (2, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=2)

    # Para el Slot 3 
    Boton_de_opciones = Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: model.acciones_del_historial (3, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=3)

    # Para el Slot 4 
    Boton_de_opciones = Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: model.acciones_del_historial (4, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=4)
    
    # Para el Slot 5 
    Boton_de_opciones = Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: model.acciones_del_historial (5, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=5)
    
    # Para el Slot 6 
    Boton_de_opciones = Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: model.acciones_del_historial (6, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=6)

    # Stringvars para los slots del historial
    valor_por_defecto = "-Vacio-"
    Slot1_str = StringVar () ; Slot1_str.set (valor_por_defecto)
    Slot2_str = StringVar () ; Slot2_str.set (valor_por_defecto)
    Slot3_str = StringVar () ; Slot3_str.set (valor_por_defecto)
    Slot4_str = StringVar () ; Slot4_str.set (valor_por_defecto)
    Slot5_str = StringVar () ; Slot5_str.set (valor_por_defecto)
    Slot6_str = StringVar () ; Slot6_str.set (valor_por_defecto)

    # Espacios para el historial
    Slot1 = Button (Memory_frame, textvariable= Slot1_str, width= "25", height= "2", command= lambda: model.reemplazar (1))
    Slot1.grid (column= 0, row= 1)   

    Slot2 = Button (Memory_frame, textvariable= Slot2_str, width= "25", height= "2", command= lambda: model.reemplazar (2))
    Slot2.grid (column= 0, row= 2)   

    Slot3 = Button (Memory_frame, textvariable= Slot3_str, width= "25", height= "2", command= lambda: model.reemplazar (3))
    Slot3.grid (column= 0, row= 3)   

    Slot4 = Button (Memory_frame, textvariable= Slot4_str, width= "25", height= "2", command= lambda: model.reemplazar (4))
    Slot4.grid (column= 0, row= 4)   

    Slot5 = Button (Memory_frame, textvariable= Slot5_str, width= "25", height= "2", command= lambda: model.reemplazar (5))
    Slot5.grid (column= 0, row= 5)
   
    Slot6 = Button (Memory_frame, textvariable= Slot6_str, width= "25", height= "2", command= lambda: model.reemplazar (6))
    Slot6.grid (column= 0, row= 6)
    
    # Borrar el contenido de todos los "Slots" del historial
    erase_historial = Button (Memory_frame, text= "🗑", font= (None, 11), command= model.clear_all, padx= "7.55")
    erase_historial.grid (column= 1, row= 0)

    # Botones del teclado de la calculadora
    Fuente_botones_calbasica = ("consolas", 12)
    
    # Digitos
    Bo0= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "0", command= lambda: model.go_to_console("0")).grid (row=5, column=0, sticky=W+E)
    Bo1= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "1", command= lambda: model.go_to_console("1")).grid (row=4, column=0, sticky=W+E)
    Bo2= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "2", command= lambda: model.go_to_console("2")).grid (row=4, column=1, sticky=W+E)
    Bo3= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "3", command= lambda: model.go_to_console("3")).grid (row=4, column=2, sticky=W+E)
    Bo4= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "4", command= lambda: model.go_to_console("4")).grid (row=3, column=0, sticky=W+E)
    Bo5= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "5", command= lambda: model.go_to_console("5")).grid (row=3, column=1, sticky=W+E)
    Bo6= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "6", command= lambda: model.go_to_console("6")).grid (row=3, column=2, sticky=W+E)
    Bo7= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "7", command= lambda: model.go_to_console("7")).grid (row=2, column=0, sticky=W+E)
    Bo8= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "8", command= lambda: model.go_to_console("8")).grid (row=2, column=1, sticky=W+E)
    Bo9= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "9", command= lambda: model.go_to_console("9")).grid (row=2, column=2, sticky=W+E)

    # Simbolos 
    B_suma= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "+", command= lambda: model.go_to_console("+")).grid (row=2, column=3, sticky=W+E)
    B_menos= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "-", command= lambda: model.go_to_console("-")).grid (row=3, column=3, sticky=W+E)
    B_multiplicacion= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "x", command= lambda: model.go_to_console("*")).grid (row=4, column=3, sticky=W+E)
    B_division= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "÷", command= lambda: model.go_to_console("/")).grid (row=5, column=3, sticky=W+E)
    BPo= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= ".", command= lambda: model.go_to_console(".")).grid (row=5, column=1, sticky=W+E)

    # Botones con funciones especiales 
    B_Potencia= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "**", command= lambda: model.go_to_console("**")); B_Potencia.grid (row=0, column=0, sticky=W+E)
    B_Parentesis1= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "(", command= lambda: model.go_to_console("(")); B_Parentesis1.grid (row=0, column=1, sticky=W+E)
    B_Parentesis2= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= ")", command= lambda: model.go_to_console(")")); B_Parentesis2.grid (row=0, column=2, sticky=W+E)
    B_ans= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "ANS", command= model.ANS); B_ans.grid (row=0, column=3, sticky=W+E)
    boeq= Button (win_bt, padx= 25, pady= 25, font= Fuente_botones_calbasica, text= "=", command= model.igual); boeq.grid (row=5, column=2, sticky=W+E)
    Clear= Button (win_bt, text= "C", font= Fuente_botones_calbasica, pady= 25, command = model.limpiar); Clear.grid (row=1, column=0, sticky=W+E)
    Erase= Button (win_bt, pady=25, font= Fuente_botones_calbasica, text= "←", command = model.delete); Erase.grid (row=1, column=1, columnspan= 3,sticky=W+E)

    # Funcion para que se restaure la ventana inicial
    def restaurar_inicio ():
        import VIEW_Ventana_de_inicio as vp
        raiz.withdraw ()
        vp.root_prueba.deiconify ()

    raiz.protocol ("WM_DELETE_WINDOW", restaurar_inicio)

# Ver operaciones guardadas
def operaciones_incloud ():
    """La Función "operaciones_incloud" accede a las operaciones guardadas en la base de datos."""
    import MODEL_firebase as connect
    import firebase_controller as inv
    from MODEL_Funciones_Calculadora_basica import reemplazar_en_la_nube
    
    operaciones_guardadas = connect.leer_operaciones (inv.True_User)

    global operaciones

    operaciones = Frame (raiz, borderwidth= 1, relief= "solid")
    operaciones.grid (column= 1, row= 1, pady= 5)
    
    Operaciones_info = Label (operaciones, text= "Operaciones guardadas en la nube", fg= "green", width= 30)
    Operaciones_info.grid (column= 0, row= 0, columnspan= 2)
    
    Usuario = Label (operaciones, text= f" Usuario accedido: {inv.True_User}", width= 30)
    Usuario.grid (column= 0, row= 1, columnspan= 2)
    
    try:
        if len(operaciones_guardadas) > 0:
            numero_de_fila = 2
            reemplazable = 1 
            
            for numero_de_iteraciones, i in enumerate (operaciones_guardadas):
                if numero_de_iteraciones == 12: # Esto es para que solo se puedan hacer 12 iteraciones
                    break
                else:
                    ops_label = Button (operaciones, text= f"{i}", width= 25, relief= "flat", background= "light green", command= lambda reemplazable1 = reemplazable: (reemplazar_en_la_nube (reemplazable1, operaciones_guardadas)))
                    ops_label.grid (column= 0, row= numero_de_fila)
                    numero_de_fila += 1
                    reemplazable += 1
            
            # Reasignacion numero de fila
            numero_de_fila = 2
            eliminable = -1
            for numero_iteraciones in enumerate (operaciones_guardadas):
                if numero_iteraciones == 12:
                    break
                else:
                    ops_button = Button (operaciones, text= "🗑", width= 5, relief= "flat", background= "Green", command= lambda eliminar = eliminable: (connect.delete_funciones (inv.True_User, eliminar, "operaciones"), update_cloud_operations ()))
                    ops_button.grid (column= 1, row= numero_de_fila)
                    numero_de_fila += 1
                    eliminable -= 1
        else:
            raise IndexError # Pasa al bloque except   
    except IndexError:
        # Cuando el usuario no tenga operaciones en la base de datos 
        # se le va a informar a través de un label
        no_operaciones = Label (operaciones, text= "No tiene operaciones guardadas en la nube")
        no_operaciones.grid (column= 0, row= 3)

# Funcion para actualizar el historial de operaciones en la nube
def update_cloud_operations():
    """La función "update_cloud_operations" actualiza la vista de los botones del historial de la base de datos."""
    import MODEL_firebase as connect
    import firebase_controller as inv
    from MODEL_Funciones_Calculadora_basica import reemplazar_en_la_nube
    
    operaciones_guardadas = connect.leer_operaciones (inv.True_User)
    
    # Este ciclo se utiliza para eliminar todos los "widgets" hijos del frame operaciones
    for widget in operaciones.winfo_children ():      
        widget.destroy ()
        
    try:
        Operaciones_info = Label (operaciones, text= "Operaciones guardadas en la nube", fg= "green", width= 30)
        Operaciones_info.grid (column= 0, row= 0, columnspan= 2)
    
        Usuario = Label (operaciones, text= f" Usuario accedido: {inv.True_User}", width= 30)
        Usuario.grid (column= 0, row= 1, columnspan= 2)
        
        if len(operaciones_guardadas) > 0:
            numero_de_fila = 2
            reemplazable = 1
            
            for numero_de_iteraciones, i in enumerate (operaciones_guardadas):
                if numero_de_iteraciones == 12: # Esto es para que solo se puedan hacer 12 iteraciones
                    break
                else:
                    ops_label = Button (operaciones, text= f"{i}", width= 25, relief= "flat", background= "light green", command= lambda reemplazable1 = reemplazable: (reemplazar_en_la_nube (reemplazable1, operaciones_guardadas)))
                    ops_label.grid (column= 0, row= numero_de_fila)
                    numero_de_fila += 1
                    reemplazable += 1
            
            # Reasignacion numero de fila
            numero_de_fila = 2
            eliminable = -1
            for numero_iteraciones in enumerate (operaciones_guardadas):
                if numero_iteraciones == 12:
                    break
                else:
                    ops_button = Button (operaciones, text= "🗑", width= 5, relief= "flat", background= "Green", command= lambda eliminar = eliminable: (connect.delete_funciones (inv.True_User, eliminar, "operaciones"), update_cloud_operations ()))
                    ops_button.grid (column= 1, row= numero_de_fila)
                    numero_de_fila += 1
                    eliminable -= 1
        else:
            raise IndexError # Pasa al bloque except   
    except IndexError:
        # Cuando el usuario no tenga operaciones en la base de datos se le va a informar a través de un label
        no_operaciones = Label (operaciones, text= "No tiene operaciones guardadas en la nube")
        no_operaciones.grid (column= 0, row= 3)