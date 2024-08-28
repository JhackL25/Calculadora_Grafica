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
    

    # Globalizacion de variables para que las utilizen las funciones
    global Slot1, Slot2, Slot3, Slot4, Slot4, Slot5, Slot6, Memory_frame, Slot1_str, Slot2_str, Slot3_str, Slot4_str, Slot5_str, Slot6_str, Entrada_funciones, raiz, Variable_de_control
    
    # Creación de la ventana de la calculadora grafica
    raiz = tk.Toplevel ()
    raiz.title ("Calculadora gráfica")

    #Opciones del menu
    Menu_principal = tk.Menu (raiz)
    raiz.config (menu= Menu_principal) #Esto es para que la barra del menu este en la esquina

    # Ubicacion de la entrada de datos
    Label_entrada = tk.Label (raiz, text= "Ingrese su función f(x) = ", font= ("Helvetica", 12))
    Label_entrada.grid (column= 0, row= 0, sticky= "we", pady= 10, padx= 10)

    Entrada_funciones = tk.Entry (raiz, font= ("Helvetica", 11), borderwidth= 1, relief= "solid")
    Entrada_funciones.grid (column= 1, row= 0, ipady= 7, sticky= "we", pady= 10)
    
# Funciones que utiliza la calculadora grafica
    # Listas en donde se almacenan temporalmente las funciones 
    Funciones_actuales = [] # Aqui se almacenan las funciones (no datos)
    Graficas = [] # Aqui se almacenan los graficos que se ven en el frame (datos de las funciones)

    # Función para graficar la función de la entrada
    def graficar_funciones(evento_enter):
        funcion = Entrada_funciones.get ()
        funcion = mod.correc_ecuacion (funcion)
        
        # En este caso limitamos al usuario para que solo pueda graficar 6 funciones
        # de manera simultanea
        if len (Funciones_actuales) >= 6:
            return print("No puedes graficar más de 6 funciones.")
            
        try:
            π = np.pi
            e = np.e   

            if 'np.tan('  in funcion:
                x_vals_tan = np.linspace(-50, 50, 100000)
                y_vals_tan = np.array([eval (funcion) for x in x_vals_tan])
    
                y_vals_tan[np.abs(y_vals_tan) > 50] = np.nan 
                
                # Si ya hay menos de 6 funciones graficadas, añadir la nueva
                grafico, = ax.plot (x_vals_tan, y_vals_tan, label=f'f {len (Funciones_actuales) + 1}(x) = {mod.correc_historial(funcion)}')
                Graficas.append (grafico)
                Funciones_actuales.append (funcion)
                print('tangente')
            else:
                # Aqui se define el dominio (x) y los valores que la funcion toma en (y)
                x_vals = np.linspace (-500, 500, 10000)
                y_vals = [eval (funcion) for x in x_vals]

                # Si ya hay menos de 6 funciones graficadas, añadir la nueva
                grafico, = ax.plot (x_vals, y_vals, label=f'f {len (Funciones_actuales) + 1}(x) = {mod.correc_historial(funcion)}')
                Graficas.append (grafico)
                Funciones_actuales.append (funcion)
                print('sin tangente')

            # Actualizacion de los botones
            Recorrer_funciones ()

            # Ajustar el gráfico
            ax.relim ()
            ax.autoscale_view ()
            ax.legend ()  # Mostrar la leyenda con las etiquetas de las funciones
            Frame_grafico.draw () # Redibujar el gráfico
            
            # Guardar la función en el historial
            mod.historial (funcion)
        except Exception as e:
            print (f"Error: {e}")

        # CODIGO ORIGINAL (UNA FUNCION)
        # # Funcion para graficar la funcion de la entrada
        # def graficar_funciones (evento_enter): 
        #     funcion = Entrada_funciones.get ()    
        #     funcion = mod.correc_ecuacion (funcion)

        #     try:
        #         x_vals = np.linspace (-500, 500, 10000)
        #         y_vals = [eval(funcion) for x in x_vals]
        #         line.set_ydata (y_vals)
        #         ax.relim ()
        #         ax.autoscale_view()
        #         Frame_grafico.draw () # ahora este reemplaza a "fig.canvas.draw_idle()"
                
        #         # Aqui se guarda la funcion en el historial
        #         mod.historial (funcion)
        #     except Exception as e:
        #         print(f"Error: {e}")

    # Vinculación de la tecla "Enter" a la funcion de graficar
    Entrada_funciones.bind ("<Return>", graficar_funciones)

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
                # Creacion del menu para seleccionar cual cuadricula deshabilitar
                Menu_irrationals = tk.Menu (raiz, tearoff= 0)

                # Funciones para reemplazar con pi o euler
                def pi_replace ():
                    Contenido_nuevo = (funcion + "π")
                    Entrada_funciones.delete (0, tk.END)
                    Entrada_funciones.insert (0, Contenido_nuevo)

                def e_replace ():
                    Contenido_nuevo = (funcion + "e")
                    Entrada_funciones.delete (0, tk.END)
                    Entrada_funciones.insert (0, Contenido_nuevo)

                #Opciones del menu
                Menu_irrationals.add_command (label= "π", command= pi_replace)
                Menu_irrationals.add_separator ()
                Menu_irrationals.add_command (label= "e", command= e_replace)
                
                Menu_irrationals.post (raiz.winfo_pointerx (), raiz.winfo_pointery ())
            
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
    
    # Funcion para graficar la funcion de la entrada en 3D
    def grafica3D():
        from tkinter import simpledialog
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

        def Graficos_3D(funcion_str, rango=(-5, 5), num_puntos=100):
            # Creamos un entorno seguro para evaluar la función
            def funcion(x, y):
                return eval(funcion_str, {"x": x, "y": y, "np": np})
            
            x = np.linspace(rango[0], rango[1], num_puntos)
            y = np.linspace(rango[0], rango[1], num_puntos)
            X, Y = np.meshgrid(x, y)
            Z = funcion(X, Y)

            Grafico_3D = plt.figure()
            ax = Grafico_3D.add_subplot (111, projection='3d')
            ax.plot_surface (X, Y, Z, cmap='viridis')

            ax.set_xlabel ('Eje X')
            ax.set_ylabel ('Eje Y')
            ax.set_zlabel ('Eje Z')

            return Grafico_3D

        # Interfaz gráfica para ingresar la función
        def obtener_funcion():
            from MODEL_grafica import correc_ecuacion2
            funcion_str = simpledialog.askstring ("Entrada de funciones 3D", "Introduce una función en términos de (x) y (y):", initialvalue="x**2 + y**2", parent= raiz)
            funcion_str = correc_ecuacion2 (funcion_str)
            return funcion_str

        funcion_str = obtener_funcion()
        if funcion_str:  # Si el usuario ingresó una función
            Ventana_3d = tk.Toplevel (raiz)
            Ventana_3d.title (f"Gráfica 3D de | {funcion_str} |")

            Grafico = Graficos_3D (funcion_str)
            Frame_3d = FigureCanvasTkAgg (Grafico, master= Ventana_3d)
            Frame_3d.get_tk_widget ().pack (fill= "both", expand= True)

            Herramientas = NavigationToolbar2Tk (Frame_3d, Ventana_3d, pack_toolbar= True)
            Herramientas.update ()
            
            global Eliminar_grafico_3D
            def Eliminar_grafico_3D ():
                try:
                    plt.close ()
                    Ventana_3d.destroy ()
                except NameError:
                    pass

        Ventana_3d.protocol ("WM_DELETE_WINDOW", Eliminar_grafico_3D)

    # Funcion para deshabilitar la cuadriculas
    def Deshabilitar_cuadriculas ():
        # Creacion del menu para seleccionar cual cuadricula deshabilitar
        Menu_cuadriculas = tk.Menu (raiz, tearoff= 0)

        # Funciones para configurar las cuadriculas mayores
        def mayorticks_on ():
            ax.xaxis.set_major_locator(plt.MultipleLocator (2.5))
            ax.yaxis.set_major_locator(plt.MultipleLocator (2.5))

        def mayorticks_off ():
            ax.xaxis.set_major_locator(plt.NullLocator ())
            ax.yaxis.set_major_locator(plt.NullLocator ())

        Menu_cuadriculas.add_command (label= "Habilitar cuadriculas mayores", command= lambda:  (mayorticks_on (), Frame_grafico.draw ()))
        Menu_cuadriculas.add_command (label= "Deshabilitar cuadriculas mayores", command= lambda: (mayorticks_off (), Frame_grafico.draw ()))
       
        Menu_cuadriculas.add_separator ()
    
        Menu_cuadriculas.add_command (label= "Habilitar cuadriculas menores", command= lambda:  (ax.minorticks_on (), Frame_grafico.draw ()))
        Menu_cuadriculas.add_command (label= "Deshabilitar cuadriculas menores", command= lambda: (ax.minorticks_off (), Frame_grafico.draw ()))

        Menu_cuadriculas.post (raiz.winfo_pointerx (), raiz.winfo_pointery ())

        # Para actualizar nuevamente el grafico se utiliza 
        # Frame_grafico.draw () que redibuja el frame de la grafica

# Creacion de widgets
    # Boton para graficar la funcion
    Graficar_button = tk.Button (raiz, text= "Graficar función", font= ("Helvetica", 11), borderwidth= 1, relief= "solid", background= "#cccccc", command= lambda: (graficar_funciones ("XD")))
    Graficar_button.grid (column= 2, row= 0, padx= 5)

    # Botones de funciones trigonometricas
    teclado_frame = tk.Frame (raiz)
    teclado_frame.grid (column= 1, row= 1)

    trigonometria = ("Potencia: ^", "Sin", "Cos", "Tan", "π/e", "CSC", "SEC", "CTAN")
    Funciones = ("Exponenciación", "Seno", "Coseno", "Tangente", "Pi", "Cosecante", "Secante", "Cotangente")
    
    # Número de fila, columna y funcion para los botones del ciclo for
    fila = 0
    Columna = 0
    funcion = 0

    # Ciclo for para los botones del teclado
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
    ax.grid (which = "major", linewidth = 1)
    ax.grid (which = "minor", linewidth = 0.2)
    ax.minorticks_on ()

    # Creacion del "Frame" del gráfico de matplot
    Frame_grafico = FigureCanvasTkAgg (fig, master= raiz)
    Frame_grafico.get_tk_widget().grid (column= 0, row= 2, columnspan= 3, sticky= "nsew", padx= 10, pady= 10)

    # Añadir la barra de herramientas de matplot a la ventana de tkinter
    Barra_de_herramientas = NavigationToolbar2Tk (Frame_grafico, raiz, pack_toolbar= False)
    Barra_de_herramientas.update ()
    Barra_de_herramientas.place (x= 362, y= 170, anchor= "center", width= 680, height= 30)

    # Grafico inicial (Esto se puede dejar de utilizar)
    # x = np.linspace (-500, 500, 10000)
    # y = 2 * x**2 + 3 * x + 1
    # line, = ax.plot (x, y)

    # Creacion del historial
    # Frame del historial
    Memory_frame = tk.Frame (raiz, borderwidth= 1, relief= "solid")
    Memory_frame.grid (column= 3, row= 0, rowspan= 3, padx= 10, pady= 10, sticky= "n")

    #Label/titulo para el historial
    Titulo = tk.Label (Memory_frame, text= "Historial", font= ("Consolas", 16))
    Titulo.grid (column= 0, row= 0)

    # Frame de la consola de funciones actuales
    Consola_funciones = tk.Frame (raiz, borderwidth= 1, relief= "solid")
    Consola_funciones.grid (column= 3, row= 2, columnspan= 2, pady= 10)

    # Titulo de la consola de funciones actuales
    Actual_functions_title = tk.Label (Consola_funciones, text= "Funciones actuales (click para eliminar)", width= 75)
    Actual_functions_title.pack ()

    # Botones de la consola 
    def Recorrer_funciones ():
        # Limpiar el frame de botones antes de crearlos de nuevo
        for widget in Consola_funciones.winfo_children():
            widget.destroy()
        
        Actual_functions_title = tk.Label (Consola_funciones, text= "Funciones actuales (click para eliminar)", width= 75)
        Actual_functions_title.pack ()
        
        # Ciclo para crear botones
        for i, funcion in enumerate (Funciones_actuales):
            Boton_funcion = tk. Button (Consola_funciones, text=f'Eliminar f{i+1}', command=lambda i=i: eliminar_funcion(i), background= "pink", relief= "flat")
            Boton_funcion.pack (fill= "x")
    
    def eliminar_funcion(indice_funcion):
        try :
            # Eliminar la función y su línea del gráfico
            Graficas [indice_funcion].remove()
            del Graficas [indice_funcion]
            del Funciones_actuales [indice_funcion]
            
            # Actualizar el gráfico
            ax.relim ()
            ax.autoscale_view ()
            
            if len (Funciones_actuales) == 0: # En caso de que ya no existan funciones 
#                                             # actuales la leyenda no va a arrojar error
                ax.legend ([""])
            else:
                ax.legend ()

            Frame_grafico.draw ()
            
            # Actualizar los botones
            Recorrer_funciones ()
        except:
            pass

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

    # Funciones especiales para la barra de herramientas de matplot
    # Imitar el estilo de la barra de herramientas
    def Cursor_dentro (evento_cursor):
        evento_cursor.widget.config (relief= "sunken")
    
    def Cursor_fuera (evento_cursor):
        evento_cursor.widget.config (relief= "flat") 

    #Boton para grafica 3D
    Grafica3D_button = tk.Button (raiz, text= "Grafica en 3D", font= ("Helvetica", 9), borderwidth= 1, relief= "flat", command= grafica3D)
    Grafica3D_button.place (x= 300, y= 170, anchor= "center")

    #Vinculacion del boton para graficar 3D al estilo
    Grafica3D_button.bind ("<Enter>", Cursor_dentro)
    Grafica3D_button.bind ("<Leave>", Cursor_fuera)

    # Boton para deshabilitar la cuadricula
    Deshabilitar_cuadricula = tk.Button (raiz, text= "Deshabilitar cuadricula", font= ("Helvetica", 9), borderwidth= 1, relief= "flat", command= Deshabilitar_cuadriculas)
    Deshabilitar_cuadricula.place (x= 420, y= 170, anchor= "center")
    
    #Vinculacion del boton para graficar 3D al estilo
    Deshabilitar_cuadricula.bind ("<Enter>", Cursor_dentro)
    Deshabilitar_cuadricula.bind ("<Leave>", Cursor_fuera)

    # Casos en donde se debe activar el modo invitado
    if Variable_de_control == False:
        # En caso de que el usuario no acceda al modo invitado se va a activar el historial de la nube y esta opcion del menu
        funciones_incloud ()
        # Menu de servicios en la nube
        from firebase_controller import search_users, modificar_datos, del_users
        cloud_services = tk.Menu (tearoff= 0)
        cloud_services.add_command (label= "Buscar su usuario", command= search_users); cloud_services.add_separator ()
        cloud_services.add_command (label= "Modificar datos del usuario", command= modificar_datos); cloud_services.add_separator ()
        cloud_services.add_command (label= "Eliminar su usuario", command= del_users)
        
        Menu_principal.add_cascade (label= "Servicios en la nube", menu= cloud_services)
    else:
        # En caso de que el usuario acceda al modo invitado se va a mostrar el siguiente mensaje 
        Menu_principal.add_command (label= "Servicios en la nube", state= "disabled")
        advertencia = tk.Label (raiz, text= "Algunas funciones se encuentran limitadas \n[Modo invitado]", font= ("Arial", 9), fg= "#9b9b9b")
        advertencia.place (relx= 0.87, rely= 0.8, anchor= "s")

    # Función para que cuando se cierre vuelva a la ventana de inicio
    def restaurar_inicio ():
        import VIEW_Calculadora_basica as basic
        raiz.destroy ()
        plt.close () # Para que se cierre el grafico, que se encuentra en el frame
        def Eliminar_graficos3d ():  # Elimina la grafica 3D
            try:
                Eliminar_grafico_3D ()
            except NameError:
                pass
        Eliminar_graficos3d ()
        basic.raiz.deiconify ()

    raiz.protocol ("WM_DELETE_WINDOW", restaurar_inicio)

    # Para cada vez que se abra el historial este limpio
    mod.Historial.clear ()
    Graficas.clear ()
    Funciones_actuales.clear ()

# Ver funciones guardadas
def funciones_incloud ():
    """La Función "funciones_incloud" accede a las funciones guardadas en la base de datos"""
    import tkinter as tk
    import MODEL_firebase as connect
    import firebase_controller as inv
    
    global Funciones
    
    funciones_guardadas = connect.leer_funcion_grafica (inv.True_User)

    Funciones = tk.Frame (raiz, borderwidth= 1, relief= "solid")
    Funciones.grid (column= 4, row= 0, sticky= "n", rowspan= 3, pady= 10)
    
    Funciones_info = tk.Label (Funciones, text= "Funciones guardadas en la nube", fg= "green", width= 30)
    Funciones_info.grid (column= 0, row= 0, columnspan= 2)
    
    Usuario = tk.Label (Funciones, text= f"Usuario accedido: {inv.True_User}", width= 30)
    Usuario.grid (column= 0, row= 1, columnspan= 2)
    
    try:
        if len(funciones_guardadas) > 0:
            numero_de_fila = 2
            reemplazable = 1

            for numero_de_iteraciones, i in enumerate (funciones_guardadas):
                if numero_de_iteraciones == 12: # Esto es para que solo se puedan hacer 12 iteraciones
                    break
                else:
                    from MODEL_grafica import reemplazar_en_la_nube

                    funcs_buttons = tk.Button (Funciones, text= f"{i}", width= 25, relief= "flat", background= "light green", command= lambda reemplazable1 = reemplazable: (reemplazar_en_la_nube (reemplazable1, funciones_guardadas)))
                    funcs_buttons.grid (column= 0, row= numero_de_fila)
                    numero_de_fila += 1
                    reemplazable += 1
            
            # Reasignacion numero de fila
            numero_de_fila = 2
            eliminable = -1
            for numero_iteraciones in enumerate (funciones_guardadas):
                if numero_iteraciones == 12:
                    break
                else:
                    ops_button = tk.Button (Funciones, text= "🗑", width= 5, relief= "flat", background= "Green", command= lambda eliminar = eliminable: (connect.delete_funciones (inv.True_User, eliminar, "funciones"), update_cloud_functions ()))
                    ops_button.grid (column= 1, row= numero_de_fila)
                    numero_de_fila += 1
                    eliminable -= 1
        else:
            raise IndexError # Pasa al bloque except   
    except IndexError:
        # Cuando el usuario no tenga operaciones en la base de datos 
        # se le va a informar a través de un label
        no_funciones = tk.Label (Funciones, text= "No tiene funciones guardadas en la nube")
        no_funciones.grid (column= 0, row= 3)

# Funcion para actualizar el historial de la nube
def update_cloud_functions():
    """La función "update_cloud_functions" actualiza la vista de los botones del historial de la base de datos."""
    import tkinter as tk
    import MODEL_firebase as connect
    import firebase_controller as inv

    # Extraccion de las funciones guardadas en la base de datos   
    funciones_guardadas = connect.leer_funcion_grafica (inv.True_User)

    # Este ciclo se utiliza para eliminar todos los "widgets" hijos del frame Funciones
    for wid in Funciones.winfo_children ():
        wid.destroy ()

    # Aqui se vuelven a crear los wigets del frame 
    try:
        Funciones_info = tk.Label (Funciones, text= "Funciones guardadas en la nube", fg= "green", width= 30)
        Funciones_info.grid (column= 0, row= 0, columnspan= 2)
    
        Usuario = tk.Label (Funciones, text= f"Usuario accedido: {inv.True_User}", width= 30)
        Usuario.grid (column= 0, row= 1, columnspan= 2)
        
        if len(funciones_guardadas) > 0:
            numero_de_fila = 2
            reemplazable = 1
            
            for numero_de_iteraciones, i in enumerate (funciones_guardadas):
                if numero_de_iteraciones == 12: # Esto es para que solo se puedan hacer 12 iteraciones
                    break
                else:
                    from MODEL_grafica import reemplazar_en_la_nube

                    funcs_buttons = tk.Button (Funciones, text= f"{i}", width= 25, relief= "flat", background= "light green", command= lambda reemplazable1 = reemplazable: (reemplazar_en_la_nube (reemplazable1, funciones_guardadas)))
                    funcs_buttons.grid (column= 0, row= numero_de_fila)
                    numero_de_fila += 1
                    reemplazable += 1
            # Reasignacion numero de fila
            numero_de_fila = 2
            eliminable = -1
            for numero_iteraciones in enumerate (funciones_guardadas):
                if numero_iteraciones == 12:
                    break
                else:
                    ops_button = tk.Button (Funciones, text= "🗑", width= 5, relief= "flat", background= "Green", command= lambda eliminar = eliminable: (connect.delete_funciones (inv.True_User, eliminar, "funciones"), update_cloud_functions ()))
                    ops_button.grid (column= 1, row= numero_de_fila)
                    numero_de_fila += 1
                    eliminable -= 1
        else:
            raise IndexError # Pasa al bloque except   
    except IndexError:
        # Cuando el usuario no tenga operaciones en la base de datos se le va a informar a través de un label
        no_funciones = tk.Label (Funciones, text= "No tiene funciones guardadas en la nube")
        no_funciones.grid (column= 0, row= 3)