
from tkinter import ttk as ttk
import tkinter as tk

#Creacion de la ventana de inicio 
def ventana_principal ():
    """La Función "ventana_principal" construye la ventana de inicio."""
    import main as run
    import MODEL_Funciones_Calculadora_basica as model
    import firebase_controller as connect

    global root_prueba

    root_prueba = tk.Tk()
    root_prueba.title ("Ventana de inicio")
    root_prueba.geometry ("810x340")
    root_prueba.resizable (False, False)

    #Label de bienvenida (con frame)
    F_bien = ttk.Frame (root_prueba)
    F_bien.pack()

    Bienvenida_C = ttk.Label(F_bien, text="Bienvenido a la \n Calculadora Grafica", font= ("Century", 38)).pack()

    #Frame del menu
    frame_menu = ttk.Frame (root_prueba)
    frame_menu.config (borderwidth= 2)
    frame_menu.pack ()

    # Registrarse
    Login_Button = ttk.Button (frame_menu, text="Registrarse", width=25, command= lambda: (root_prueba.withdraw (), connect.registro ())); Login_Button.grid (row=0, column=0, sticky= "NS", padx= 30, pady= 50)

    #Acceder
    Acceder = ttk.Button (frame_menu, text="Acceder", width=25, command= lambda: (connect.Acceder (), root_prueba.withdraw ())); Acceder.grid (row=0, column=1, sticky="NS", padx= 30, pady= 50)
 
    def iniciar_modo_invitado ():
        from tkinter import Label
        import VIEW_Calculadora_basica as view
        view.Variable_de_control = True
        
        view.Menu_principal.add_command (label= "Servicios en la nube", state= "disabled")
        advertencia = Label (view.raiz, text= "Algunas funciones se encuentran limitadas \n[Modo invitado]", font= ("Arial", 9), fg= "#9b9b9b")
        advertencia.place (relx= 0.784, rely= 0.8, anchor= "s")

    #Ingresar como invitado
    Acceder_como_invitado = ttk.Button (frame_menu, text= "Acceder como invitado", width= 25, command= lambda: (root_prueba.withdraw (), model.Historial.clear (), run.run (), iniciar_modo_invitado (), model.limpiar ()))
    Acceder_como_invitado.grid (row= 2, column= 0, columnspan= 2, sticky="NS", pady= 50)

    # # Funcion para eliminar todo
    # def finalizar_experiencia ():
    #     try:
    #         from VIEW_cal_grafica import raiz as raiz_grafica
    #         from VIEW_Calculadora_basica import raiz as raiz_basica
    #         root_prueba.destroy ()
    #         raiz_basica.destroy ()
    #         raiz_grafica.destroy ()
    #     except Exception as e:
    #         if e:
    #             root_prueba.destroy ()
    #         else:
    #             root_prueba.destroy ()

    # # Vinculación del "cerrado de aplicacion con "finalizar_experencia""
    # root_prueba.protocol ("WM_DELETE_WINDOW", finalizar_experiencia)

    root_prueba.mainloop ()