# Funcion experimental para recrear la ventana en tkinter 

def cal_graf_tkinter_vs ():
    # Importacion de GUI tkinter
    from tkinter import ttk as ttk
    import tkinter as tk
    import MODEL_grafica as mod

    # Importaciones de matplot
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from mpl_toolkits.mplot3d import axes3d

    # Globalizacion de variables para que las utilizen las funciones
    global Slot1, Slot2, Slot3, Slot4, Slot4, Slot5, Slot6, Memory_frame, Slot1_str, Slot2_str, Slot3_str, Slot4_str, Slot5_str, Slot6_str, Entrada_funciones, raiz, Variable_de_control
    
    # Creación de la ventana de la calculadora grafica
    raiz = tk.Toplevel ()
    raiz.title ("Calculadora gráfica")

    #Opciones del menu
    Menu_principal = tk.Menu (raiz)
    raiz.config (menu= Menu_principal) #Esto es para que la barra del menu este en la esquina

    Menu_principal.add_command (label= "Calculadora gráfica")
    Menu_principal.add_command (label= "Calculadora básica")
    Menu_principal.add_command (label= "Servicios en la nube")

    # Ubicacion de la entrada de datos
    Label_entrada = tk.Label (raiz, text= "Ingrese su función f(x) = ", font= ("Helvetica", 12))
    Label_entrada.grid (column= 0, row= 0, sticky= "we", pady= 10, padx= 10)

    Entrada_funciones = tk.Entry (raiz, font= ("Helvetica", 11), borderwidth= 1, relief= "solid") #, background= "#eeeeee")
    Entrada_funciones.grid (column= 1, row= 0, ipady= 7, sticky= "we", pady= 10)
    
# Funciones que utiliza la calculadora grafica
    
    # Funcion para graficar la funcion de la entrada
    def graficar_funcion (evento_enter):
        
        funcion = Entrada_funciones.get ()    
        funcion = mod.correc_ecuacion (funcion)

        try:
            x_vals = np.linspace (-500, 500, 10000)
            y_vals = [eval(funcion) for x in x_vals]
            line.set_ydata (y_vals)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw_idle()
        
            # Aqui se guarda la funcion en el historial
            mod.historial (funcion)
        except Exception as e:
            print(f"Error: {e}")

    # Vinculación de la tecla "Enter" a la funcion de graficar
    Entrada_funciones.bind ("<Return>", graficar_funcion)

    # Funcion para cada boton del ciclo for
    def funciones_graficas (numero_de_funcion):
        """La función "funciones_graficas" tiene el objetivo de asignar una función a cada boton 
        de funciones."""
        
        # Obtener las "funciones" de la entrada de datos
        funcion = Entrada_funciones.get ()
        
        try:
            if numero_de_funcion == "Exponenciación":
                Contenido_nuevo = (funcion + "**")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
            
            if numero_de_funcion == "Seno":
                Contenido_nuevo = (funcion + "sin()")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
            
            if numero_de_funcion == "Coseno":
                Contenido_nuevo = (funcion + "cos()")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
        
            if numero_de_funcion == "Tangente":
                Contenido_nuevo = (funcion + "tan()")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
            
            if numero_de_funcion == "Pi":
                Contenido_nuevo = (funcion + "π")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
            
            if numero_de_funcion == "Cosecante":
                Contenido_nuevo = (funcion + "csc()")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
            
            if numero_de_funcion == "Secante":
                Contenido_nuevo = (funcion + "sec()")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)

            if numero_de_funcion == "Cotangente":
                Contenido_nuevo = (funcion + "ctn()")
                Entrada_funciones.delete (0, tk.END)
                Entrada_funciones.insert (0, Contenido_nuevo)
        
        except:
            pass

# Creacion de widgets
    # Boton para graficar la funcion
    Graficar_button = tk.Button (raiz, text= "Graficar función", font= ("Helvetica", 11), borderwidth= 1, relief= "solid", background= "#cccccc", command= lambda: (graficar_funcion ('porque xD?')))
    Graficar_button.grid (column= 3, row= 0, padx= 5)

    #Boton para grafica 3D
    Grafica3D_button = tk.Button (raiz, text= "Grafica en 3D", font= ("Helvetica", 11), borderwidth= 1, relief= "solid", background= "#cccccc", command= lambda: (grafica3D("XD")))
    Grafica3D_button.grid(column= 4, row= 2, padx= 5)

    # Botones de funciones trigonometricas
    teclado_frame = tk.Frame (raiz)
    teclado_frame.grid (column= 1, row= 1)

    trigonometria = ("Potencia: ^", "Sin", "Cos", "Tan", "π", "CSC", "SEC", "CTAN")
    Funciones = ("Exponenciación", "Seno", "Coseno", "Tangente", "Pi", "Cosecante", "Secante", "Cotangente")
    
    # Número de fila, columna y funcion para los botones del ciclo for
    fila = 0
    Columna = 0
    funcion = 0

    # Estilo de los botones (solo para ttk) / no admite ni relief ni boderwidth 
    # Estilo_botones_funciones = ttk.Style ()
    # Estilo_botones_funciones.configure ("Funciones.TButton", font= ("Helvetica", 11))

    for cada_funcion in trigonometria:        
        Botones_trigonometria = tk.Button (teclado_frame, text= cada_funcion, command= lambda indice = funcion: funciones_graficas (Funciones [indice]), width= 10, pady= 5, font= ("Helvetica", 11), borderwidth= 1, relief= "solid", background= "#cccccc")
        Botones_trigonometria.grid (column= Columna, row= fila, padx= 2, pady= 3)
        Columna += 1
        funcion += 1
        
        if cada_funcion == "Tan":
            Columna = 0
            fila = 1
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots (figsize= (6, 5))
    ax.set_xlim (-10, 10)    
    ax.set_ylim (-10, 10)
#   plt.subplots_adjust (0.05,0.05,0.6,0.71) # Este codigo ya no se utiliza 
#                                            # por que no deja centrar el grafico en el frame
    ax.grid (which = "major", linewidth = 1)
    ax.grid (which = "minor", linewidth = 0.2)
    ax.minorticks_on ()

    # Creacion del "Frame" del gráfico de matplot
    Frame_grafico = FigureCanvasTkAgg (fig, master= raiz)
    Frame_grafico.get_tk_widget().grid (column= 0, row= 2, columnspan= 4, sticky= "nsew", padx= 10, pady= 10)

    # Añadir la barra de herramientas de matplot a la ventana de tkinter
    Barra_de_herramientas = NavigationToolbar2Tk (Frame_grafico, raiz, pack_toolbar= False)
    Barra_de_herramientas.update ()
    Barra_de_herramientas.place (x= 362, y= 170, anchor= "center", width= 680, height= 30)
    
    # Esta linea de codigo se descarta ya que ubica mal el widget al aumentar la resolucion
    # de la pantalla
    
    ## Barra_de_herramientas.place (relx= 0.5, rely= 0.2885, anchor= "center", width= 400, height= 30) 

    # Grafico inicial
    x = np.linspace (-500, 500, 10000)
    y = 2 * x**2 + 3 * x + 1
    line, = ax.plot (x, y)

    # Creacion del historial
    # Frame del historial
    Memory_frame = tk.Frame (raiz, borderwidth= 1, relief= "solid")
    Memory_frame.grid (column= 4, row= 0, rowspan= 4, padx= 10, pady= 10, sticky= "n")
    
    # Memory_frame.place (relx= 0.785, rely= 0.02, anchor= "n")

    #Label/titulo para el historial
    Titulo = tk.Label (Memory_frame, text= "Historial", font= ("Consolas", 16))
    Titulo.grid (column= 0, row= 0)

    # Widgets de la vista, en este caso corresponden al teclado
    # Espacios para las opciones de los slots del historial

    # Variable para el modo invitado
    from VIEW_Calculadora_basica import Variable_de_control
    
    # Para el Slot 1 
    Boton_de_opciones = tk.Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: mod.acciones_del_historial (1, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=1)

    # Para el Slot 2
    Boton_de_opciones = tk.Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: mod.acciones_del_historial (2, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=2)

    # Para el Slot 3 
    Boton_de_opciones = tk.Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: mod.acciones_del_historial (3, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=3)

    # Para el Slot 4 
    Boton_de_opciones = tk.Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: mod.acciones_del_historial (4, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=4)
    
    # Para el Slot 5 
    Boton_de_opciones = tk.Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: mod.acciones_del_historial (5, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=5)
    
    # Para el Slot 6 
    Boton_de_opciones = tk.Button (Memory_frame, text= "...", width= "5", height= "2", command= lambda: mod.acciones_del_historial (6, invitado= Variable_de_control))
    Boton_de_opciones.grid (column= 1, row=6)

    # Stringvars para los slots del historial
    valor_por_defecto = "-Vacio-"
    Slot1_str = tk.StringVar () ; Slot1_str.set (valor_por_defecto)
    Slot2_str = tk.StringVar () ; Slot2_str.set (valor_por_defecto)
    Slot3_str = tk.StringVar () ; Slot3_str.set (valor_por_defecto)
    Slot4_str = tk.StringVar () ; Slot4_str.set (valor_por_defecto)
    Slot5_str = tk.StringVar () ; Slot5_str.set (valor_por_defecto)
    Slot6_str = tk.StringVar () ; Slot6_str.set (valor_por_defecto)

    # Espacios para el historial
    Slot1 = tk.Button (Memory_frame, textvariable= Slot1_str, width= "25", height= "2", command= lambda: mod.reemplazar (1))
    Slot1.grid (column= 0, row= 1)   

    Slot2 = tk.Button (Memory_frame, textvariable= Slot2_str, width= "25", height= "2", command= lambda: mod.reemplazar (2))
    Slot2.grid (column= 0, row= 2)   

    Slot3 = tk.Button (Memory_frame, textvariable= Slot3_str, width= "25", height= "2", command= lambda: mod.reemplazar (3))
    Slot3.grid (column= 0, row= 3)   

    Slot4 = tk.Button (Memory_frame, textvariable= Slot4_str, width= "25", height= "2", command= lambda: mod.reemplazar (4))
    Slot4.grid (column= 0, row= 4)   

    Slot5 = tk.Button (Memory_frame, textvariable= Slot5_str, width= "25", height= "2", command= lambda: mod.reemplazar (5))
    Slot5.grid (column= 0, row= 5)
   
    Slot6 = tk.Button (Memory_frame, textvariable= Slot6_str, width= "25", height= "2", command= lambda: mod.reemplazar (6))
    Slot6.grid (column= 0, row= 6)

    # Borrar el contenido de todos los "Slots" del historial
    erase_historial = tk.Button (Memory_frame, text= "🗑", font= (None, 11), command= mod.clear_all, padx= "7.55")
    erase_historial.grid (column= 1, row= 0)
    
    # Función para que cuando se cierre vuelva a la ventana de inicio
    def restaurar_inicio ():
        import VIEW_Calculadora_basica as basic
        raiz.destroy ()
        plt.close () # Para que se cierre el grafico, que se encuentra en el frame
        basic.raiz.deiconify ()

    raiz.protocol ("WM_DELETE_WINDOW", restaurar_inicio)

    if Variable_de_control == False:
        funciones_incloud ()
    else:
        advertencia = tk.Label (raiz, text= "Algunas funciones se encuentran limitadas \n[Modo invitado]", font= ("Arial", 9), fg= "#9b9b9b")
        advertencia.place (relx= 0.87, rely= 0.8, anchor= "s")
    
    def grafica3D(funcion):
    # Obtener la función de la entrada
        funcion = Entrada_funciones.get()
        funcion = mod.correc_ecuacion(funcion)
        
        try:
            # Crear un nuevo eje en 3D
            fig3d = plt.figure(figsize=(6, 5))
            ax3d = fig3d.add_subplot(111, projection='3d')
            
            # Crear datos para la gráfica 3D
            x_vals = np.linspace(-5, 5, 100)
            y_vals = np.linspace(-5, 5, 100)
            x, y = np.meshgrid(x_vals, y_vals)
            
            # Evaluar la función Z = f(X, Y)
            z = eval(funcion)

            # Graficar la superficie
            ax3d.plot_surface(x, y, z, cmap='viridis')

            # Añadir etiquetas
            ax3d.set_xlabel('X axis')
            ax3d.set_ylabel('Y axis')
            ax3d.set_zlabel('Z axis')
            
            # Mostrar la gráfica
            fig3d.show()
            
        except Exception as e:
            print(f"Error: {e}")




# Ver funciones guardadas
def funciones_incloud ():
    import tkinter as tk
    import MODEL_firebase as connect
    import firebase_controller as inv
    
    operaciones_guardadas = connect.leer_funcion_grafica (inv.True_User)

    global operaciones
    
    operaciones = tk.Frame (raiz, borderwidth= 1, relief= "solid")
    operaciones.grid (column= 5, row= 1, rowspan= 4, sticky= "n")
    
    Operaciones_info = tk.Label (operaciones, text= "Funciones guardadas en la nube", fg= "green", width= 30)
    Operaciones_info.grid (column= 0, row= 0, columnspan= 2)
    
    Usuario = tk.Label (operaciones, text= f" Usuario accedido: {inv.True_User}", width= 30)
    Usuario.grid (column= 0, row= 1)
    
    try:
        if len(operaciones_guardadas) > 0:
            numero_de_fila = 2
            reemplazable = 1

            for numero_de_iteraciones, i in enumerate (operaciones_guardadas):
                if numero_de_iteraciones == 12: # Esto es para que solo se puedan hacer 12 iteraciones
                    break
                else:
                    from MODEL_grafica import reemplazar_en_la_nube

                    ops_label = tk.Button (operaciones, text= f"{i}", width= 30, background= "light green", command= lambda reemplazable1 = reemplazable: (reemplazar_en_la_nube (reemplazable1, operaciones_guardadas)))
                    ops_label.grid (column= 0, row= numero_de_fila)
                    numero_de_fila += 1
                    reemplazable += 1
        else:
            raise IndexError # Pasa al bloque except   
    except IndexError:
        # Cuando el usuario no tenga operaciones en la base de datos 
        # se le va a informar a través de un label
        no_operaciones = tk.Label (operaciones, text= "No tiene funciones guardadas en la nube")
        no_operaciones.grid (column= 0, row= 3)


    