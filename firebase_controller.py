

from tkinter import *
from tkinter import messagebox 
import MODEL_firebase as connections

#Funciones para la vista del menu de la base de datos
#Funcion para abrir el registro
def registro ():
    raiz_registro = Toplevel()
    raiz_registro.geometry("400x190")
    raiz_registro.resizable(False, False)

    entradas = Frame(raiz_registro)
    raiz_registro.title("Registro de usuarios")
    entradas.pack()
    
    Bienvenida_Entry = Label (entradas, text="Cree su usuario", font= (None, 20)).grid(row=0, column=0, columnspan=2)

    #Creacion de los nombres de las entradas 
    Label_nombre = Label (entradas, text="Usuario"); Label_nombre.grid(row=1, column=0)    
    Label_contraseña = Label (entradas, text= "Contraseña"); Label_contraseña.grid (row=2, column= 0)
    Label_edad = Label (entradas, text="Edad"); Label_edad.grid(row=3, column=0)
    Label_sexo = Label (entradas, text="Sexo"); Label_sexo.grid(row=4, column=0)
    Label_rol = Label (entradas, text="Rol"); Label_rol.grid(row=5, column=0)

    #Variables para almacemar datos
    nombre = StringVar()
    edad = StringVar()
    sexo = StringVar()
    rol = StringVar()
    contraseña = StringVar ()
      
    #Creacion de las entradas de datos
    Entrada_nombre = Entry(entradas, textvariable= nombre, width=50); Entrada_nombre.grid(row=1, column=1)
    Entrada_contraseña = Entry (entradas, textvariable= contraseña, width=50); Entrada_contraseña.grid(row=2, column=1)
    Entrada_edad = Entry(entradas, textvariable= edad, width=50); Entrada_edad.grid(row=3, column=1)
    Entrada_sexo = Entry(entradas, textvariable= sexo, width=50); Entrada_sexo.grid(row=4, column=1)
    Entrada_rol = Entry(entradas, textvariable= rol, width=50); Entrada_rol.grid(row=5, column=1)

    #boton para cargar la informacion a la base de datos y
    #funcion para mostrar que la informacion se subio correctamente
    
    def enviar_info():
        try:
            Name = nombre.get ()
            Password = contraseña.get ()
            Age = edad.get ()
            Sex = sexo.get()
            Rol = rol.get ()
            
            if Name == "" or Age == "" or Sex == "" or Rol == "" or Password == "":
                incomplete = Label (entradas, text= "Debe llenar todas las entradas de datos")
                incomplete.grid (row=6, column=0, columnspan= 2)
            
            else:
                #Aqui se crea el usuario y la contraseña
                import VIEW_Ventana_de_inicio as vp
                estado_de_registro = connections.create (Name, Age, Sex, Rol, Password)

                if estado_de_registro == True:
                    #Esto es parte del apartado estético
                    success = Label(entradas, text="Su información ha ingresado a \n la base de datos correctamente", font=("Helvetica", 14), padx=400, pady=170)
                    success.place(relx=0.5, rely=0.5, anchor="center")

                    terminar_registro = Button (entradas, text="Terminar con el registro", command= lambda: (raiz_registro.destroy (), vp.root_prueba.deiconify ()))
                    terminar_registro.place(relx=0.5, rely=0.8, anchor="center")
                else:
                    already_created = Label(entradas, text="Ya existe un usuario registrado \n con el mismo nombre de usuario", font=("Helvetica", 14), padx=400, pady=170)
                    already_created.place(relx=0.5, rely=0.5, anchor="center")

                    volver_al_registro = Button (entradas, text="Volver a la ventana de registro", command= lambda: (already_created.destroy (), volver_al_registro.destroy ()))
                    volver_al_registro.place(relx=0.5, rely=0.8, anchor="center")

        except:          
            failure = Label(entradas, text="Ha ocurrido un error su \n información no se ha enviado", font=("Helvetica", 14), padx=400, pady=170)
            failure.place(relx=0.5, rely=0.5, anchor="center")        

            reintentar = Button(entradas, text="Volver a la ventana de registro", command= lambda: (failure.destroy (), reintentar.destroy()))
            reintentar.place(relx=0.5, rely=0.8, anchor="center")

    Enviar = Button(entradas, text="Enviar información", command= enviar_info).grid(row=7, column=0, columnspan=2)
    
    def restaurar_inicio ():
        import VIEW_Ventana_de_inicio as vp
        raiz_registro.destroy ()
        vp.root_prueba.deiconify ()

    raiz_registro.protocol ("WM_DELETE_WINDOW", restaurar_inicio)

#Funcion para acceder como usuario registrado
def Acceder ():
    
    raiz_acceso = Toplevel ()
    raiz_acceso.geometry("400x125")
    raiz_acceso.resizable(False, False)

    entradas = Frame(raiz_acceso)
    raiz_acceso.title("Acceso a la base de datos")
    entradas.pack()
    
    Bienvenida_Entry = Label (entradas, text="Acceda con su usuario y contraseña", font= (None, 14)).grid(row=0, column=0, columnspan=2)

    #Creacion de los nombres de las entradas 
    Label_nombre = Label (entradas, text="Usuario"); Label_nombre.grid(row=1, column=0)    
    Label_contraseña = Label (entradas, text= "Contraseña"); Label_contraseña.grid (row=2, column= 0)

    #Variables para almacemar datos
    nombre = StringVar()
    contraseña = StringVar ()
      
    #Creacion de las entradas de datos
    Entrada_nombre = Entry(entradas, textvariable= nombre, width=50); Entrada_nombre.grid(row=1, column=1)
    Entrada_contraseña = Entry (entradas, textvariable= contraseña, width=50); Entrada_contraseña.grid(row=2, column=1)

    #boton para cargar la informacion a la base de datos y
    #funcion para mostrar que la informacion se subio correctamente
    
    def comprobar():
        import MODEL_Funciones_Calculadora_basica as model
        try:
            Name = nombre.get ()
            Password = contraseña.get ()
            
            if Name == "" or Password == "":
                incomplete = Label (entradas, text= "Debe llenar todas las entradas de datos")
                incomplete.grid (row=6, column=0, columnspan= 2)
            
            else:
                #Aqui se crea el usuario y la contraseña
                global True_User
                Estado_de_acceso = connections.acceso_usuarios (Name, Password)

                if Estado_de_acceso == Name:
                    #Se ingresa correctamente y se abre la ventana de la calculadora grafica
                    #success = Label(entradas, text="Su información ha ingresado a \n la base de datos correctamente", font=("Helvetica", 14), padx=400, pady=170)
                    #success.place(relx=0.5, rely=0.5, anchor="center")

                    import main as run
                    import VIEW_Calculadora_basica as runner
                    
                    run.run () # Ejecuta la calculadora basica
                    True_User = Estado_de_acceso # Almacena el nombre de usuario
                    runner.operaciones_incloud () # Busca operaciones con el nombre de usuario proporcionado
                    # Menu de servicios en la nube
                    cloud_services = Menu (tearoff= 0)
                    cloud_services.add_command (label= "Buscar su usuario", command= search_users); cloud_services.add_separator ()
                    cloud_services.add_command (label= "Modificar datos del usuario", command= modificar_datos); cloud_services.add_separator ()
                    cloud_services.add_command (label= "Eliminar su usuario", command= del_users)
                    
                    runner.Menu_principal.add_cascade (label= "Servicios en la nube", menu= cloud_services)

                    raiz_acceso.destroy () # Destruye la ventana de acceso a la base de datos
                    model.Historial.clear () ; model.limpiar () # Limpia el historial y la consola cuando se cierre la calculadora básica

                else:
                    incomplete = Label (entradas, text= "Contraseña o usuario incorrectos")
                    incomplete.grid (row=6, column=0, columnspan= 2)
        except:    
            def restore_log ():
                failure.destroy ()
                reintentar.destroy()
            
            failure = Label(entradas, text= "Ha ocurrido un error \n no se puede ingresar a la base de datos", font= ("Helvetica", 14), padx= 400, pady= 170)
            failure.place(relx=0.5, rely=0.5, anchor="center")        

            reintentar = Button(entradas, text= "Volver a la ventana de registro", command= restore_log)
            reintentar.place(relx=0.5, rely=0.9, anchor="center")

    Enviar = Button(entradas, text= "Enviar información", command= comprobar).grid(row= 7, column= 0, columnspan= 2, pady= 5)

    def restaurar_inicio ():
        import VIEW_Ventana_de_inicio as vp
        raiz_acceso.destroy ()
        vp.root_prueba.deiconify ()

    raiz_acceso.protocol ("WM_DELETE_WINDOW", restaurar_inicio)

#Función para buscar usuarios
def search_users():
    raiz = Toplevel()  # Crear una nueva ventana secundaria
    raiz.title("Buscar usuarios")
    raiz.resizable (False, False)
    
    search_frame = Frame(raiz)
    search_frame.pack()
    
    #Intrucciones sobre la funcion de la busqueda 
    Instruccion = Label(search_frame, text="Introduzca el nombre de usuario que desea buscar", font=(None, 14))
    Instruccion.grid(row=0, column=0, columnspan=2)
    
    #Variable para mostrar si se encontró el usuario o no
    result = StringVar()
    
    def mostrar():
        reemplazable = Entrada_us.get() #Aqui se declara la variable antes de usarse para que no ocurran errores
        try:
            if reemplazable == "":
                result.set ("Debe ingresar un nombre de usuario")
            
            elif connections.read (reemplazable) == False:
                result.set(f"El usuario | {reemplazable} | no fue encontrado o no existe")
                restore = Button (search_frame,text="Restaurar", command= lambda: (result.set (""), restore.destroy()))
                restore.grid (row=3, column=0, columnspan= 2)
            
            else:
                #Aqui se utiliza la funcion read del model de la base
                #de datos, el codigo original se cambio a conveniencia para hacer el menu
                if connections.read (reemplazable) == True:
                    result.set(f"El usuario | {reemplazable} | se encuentra registrado en la base de usuarios")
                    del_search= Button (search_frame, text= "Cerrar ventana de busqueda", command= lambda: raiz.destroy())
                    del_search.grid (row=4, column=0, columnspan= 2)
        except:
            #Aquí no pasa nada, solo es para cubrir el hecho de que aún 
            #no encuentro excepciones "reales" ¯/_(ツ)_/¯
            pass
    
    #Entry, label y boton de busqueda
    Entrada_us = Entry(search_frame, width=60)
    Entrada_us.grid(row=1, column=0)
    
    Search_Button = Button(search_frame, text="Buscar", command= mostrar)
    Search_Button.grid(row=1, column=1)
    
    result_search = Label(search_frame, textvariable=result)  
    result_search.grid(row=2, column=0, columnspan=2)
    
    raiz.mainloop()

#Funcion para modificar datos
def modificar_datos ():
    mod_raiz = Toplevel()  # Crear una nueva ventana secundaria
    mod_raiz.title("Modificar datos")
    mod_raiz.resizable (False, False)
    
    #Frame 
    mod_frame = Frame (mod_raiz)
    mod_frame.pack()

    #Instrucciones
    Instruccion_label = Label (mod_frame, text= "Ingrese el usuario para modificar sus datos \n debe estar registrado en la base de datos", font= (None, 16))
    Instruccion_label.grid (row= 0, column= 0, columnspan= 2)

    Sugerencia_label= Label (mod_frame, bg= "light gray", text= "Si quiere comprobar que \n su usuario se encuentra registrado \n puede verificarlo aqui: \n" "\n ")
    Sugerencia_label.grid (row=0, column= 2)

    #Boton para buscar el usuario dentro de la secuencia 
    Loged_us =  Button (Sugerencia_label, text= "Comprobar", command= search_users)
    Loged_us.place (relx= 0.5, y= 50, anchor= "n")

    #Entrada para buscar el usuario
    User_entry = Entry (mod_frame, width= 50)
    User_entry.grid (row= 1, column=0)

    #Frame y widgets donde se muestran las opciones para modificar informacion de usuario
    mod_options = Frame (mod_frame)
    mod_options.grid (row=3, column=0, columnspan=3)
    
    #Variable para la funcion "mod_data"
    mod_dat = StringVar ()

    #Label para ver el resultado de la busqueda para modificar el usuario
    options_label = Label (mod_frame, textvariable= mod_dat)
    options_label.grid (row=2, column=0, columnspan=3)

#Funciones que se utilizan en cada opcion de modificación 
    def mod_edad ():
    #funcion que utiliza mod mod_edad
        def try_edad ():
            #Aqui se obtiene la nueva edad de la entrada que esta en la ventana de edad 
            # se llama --> "entrada_edad"
            new_age = entrada_edad.get ()
            user_exist = User_entry.get ()
            try:
                if new_age == "":
                    add_ex.set ("Debe ingresar un nuevo valor de edad")
                else:
                    if connections.read (user_exist) != False:
                        #Aqui se utiliza la funcion update que esta en el model
                        connections.update (user_exist, key= "edad", val= new_age)
                        
                        #Esto se encarga del apartado visual del la ventana de modificación
                        label_exito = Label (raiz_edad, text= "Edad modificada correctamente", font= (None, 16), padx= 300, pady= 100)
                        label_exito.place (relx= 0.5, rely= 0.3, anchor= "center")
                        
                        cerrar_ventana_edad = Button (raiz_edad, text= "Cerrar ventana de modificación de edad", command= lambda: raiz_edad.destroy())               
                        cerrar_ventana_edad.place (relx= 0.5, rely= 0.6, anchor= "center")
                    else:
                        #Aqui se utiliza la keyword raise para que en caso de que el usuario modifique 
                        #el usuario en la ventana de busqueda mientras esta en la ventana de modificacion de edad
                        #y luego trate de modificar la edad, se dirija a la excepción, porque genera un error
                        raise ValueError
            except:    
                label_fracaso = Label (raiz_edad, text= "Ha ocurrido un error \n no se pudo modificar la edad", font= (None, 16), padx= 300, pady= 100)
                label_fracaso.place (relx= 0.5, rely= 0.3, anchor= "center")

                restaurar_edad = Button (raiz_edad, text= "Restaurar", command= lambda: (label_fracaso.destroy(), restaurar_edad.destroy()))
                restaurar_edad.place (relx= 0.5, rely= 0.7, anchor= "center")
        
        raiz_edad = Toplevel (mod_raiz)
        raiz_edad.geometry ("300x100")
        raiz_edad.title ("Modificar edad")
        raiz_edad.resizable (False, False)

        #Label de instrucción y entrada para ingresar la nueva edad
        Label_edad = Label (raiz_edad, text= "Ingrese la nueva edad del usuario", font= (None, 15))
        Label_edad.grid (row= 0, column= 0)

        entrada_edad = Entry (raiz_edad, width= 30)
        entrada_edad.grid (row= 1, column= 0)
        
        enviar_edad = Button (raiz_edad, text= "enviar", command= try_edad)
        enviar_edad.grid (row= 3, column= 0)
        
        #Label y stringvar para mostrar alguna excepción en la edad
        add_ex= StringVar ()
        except_label = Label (raiz_edad, textvariable= add_ex)
        except_label.grid (row= 2, column= 0, columnspan= 2)

    def mod_sexo ():
        def try_sex ():
            new_sex = User_entry.get ()
            filtro = filtrar_sexo.get ()
            try:
                if connections.read (new_sex) == True:
                    opcion_masculina = filtro == "Masculino"
                    opcion_femenina = filtro == "Femenino"

                    if opcion_masculina or opcion_femenina == True:
                        #Aqui se utiliza de nuevo la funcion update para modificar el sexo del usuario
                        connections.update (new_sex, key= "sexo", val= filtro)
                        label_exito = Label (raiz_sex, text= "Sexo modificado correctamente", font= (None, 16), padx= 300, pady= 100)
                        label_exito.place (relx= 0.5, rely= 0.3, anchor= "center")
                        
                        cerrar_ventana_sexo = Button (raiz_sex, text= "Cerrar ventana de modificación de sexo", command= lambda: raiz_sex.destroy())               
                        cerrar_ventana_sexo.place (relx= 0.5, rely= 0.75, anchor= "center")
                else:
                    #Aqui pasa lo mismo que en la ventana de modificación de edad
                    raise ValueError
            except:
                label_fracaso = Label (raiz_sex, text= "Ha ocurrido un error \n no se pudo modificar su sexo", font= (None, 12), padx= 300, pady= 100)
                label_fracaso.place (relx= 0.5, rely= 0.27, anchor= "center")

                restaurar_edad = Button (raiz_sex, text= "Restaurar", command= lambda: (label_fracaso.destroy(), restaurar_edad.destroy()))
                restaurar_edad.place (relx= 0.5, rely= 0.75, anchor= "center")
                        
        #Aqui se crea la ventana para modificar el sexo
        raiz_sex = Toplevel (mod_raiz)
        raiz_sex.geometry ("300x65")
        raiz_sex.resizable (False, False)

        #Label de instrucción
        label_sex = Label (raiz_sex, text= "Seleccione la opcion que desee", font= (None, 16))
        label_sex.grid (row= 0, column= 0, columnspan= 2)

        #Stringvar para modificar el sexo 
        #Esta Stringvar se utiliza como "filtro" dentro de la función try sex
        filtrar_sexo = StringVar ()
        
        #Botones para selección 
        Opcion_1 = Button (raiz_sex, text= "Femenino", command= lambda: (filtrar_sexo.set ("Femenino"), try_sex ()))
        Opcion_1.grid (row= 1, column=0)

        Opcion_2 = Button (raiz_sex, text= "Masculino", command= lambda: (filtrar_sexo.set ("Masculino"), try_sex ()))
        Opcion_2.grid (row= 1, column= 1)

    def mod_rol ():
        def try_rol ():
            new_rol = User_entry.get ()
            filtro_de_roles = filtrar_rol.get ()
            try:
                if connections.read (new_rol) == True:
                    opcion_profesor = filtro_de_roles == "Profesor"
                    opcion_estudiante = filtro_de_roles == "Estudiante"
                    
                    if opcion_profesor or opcion_estudiante == True:
                        #Aqui se utiliza de nuevo la funcion update para modificar el sexo del usuario
                        connections.update (new_rol, key= "rol", val= filtro_de_roles)
                        label_exito = Label (raiz_rol, text= "Rol modificado correctamente", font= (None, 15), padx= 300, pady= 100)
                        label_exito.place (relx= 0.5, rely= 0.3, anchor= "center")
                    
                        cerrar_ventana_rol = Button (raiz_rol, text= "Cerrar ventana de modificación de roles", command= lambda: raiz_rol.destroy())               
                        cerrar_ventana_rol.place (relx= 0.5, rely= 0.75, anchor= "center")
                else:
                    #Aqui pasa lo mismo que en la ventana de modificación de edad
                    raise ValueError   
            except: 
                label_fracaso = Label (raiz_rol, text= "Ha ocurrido un error \n no se pudo modificar su rol", font= (None, 12), padx= 300, pady= 100)
                label_fracaso.place (relx= 0.5, rely= 0.27, anchor= "center")

                restaurar_edad = Button (raiz_rol, text= "Restaurar", command= lambda: (label_fracaso.destroy(), restaurar_edad.destroy()))
                restaurar_edad.place (relx= 0.5, rely= 0.75, anchor= "center")
        
                
        #Aqui se crea la ventana para modificar el sexo
        raiz_rol = Toplevel (mod_raiz)
        raiz_rol.geometry ("270x65")
        raiz_rol.resizable (False, False)

        #Label de instrucción
        label_sex = Label (raiz_rol, text= "Seleccione el rol que desee", font= (None, 16))
        label_sex.grid (row= 0, column= 0, columnspan= 2)

        #Stringvar para modificar el rol 
        #Esta Stringvar se utiliza como "filtro" dentro de la función try rol
        filtrar_rol = StringVar ()

        #Botones para selección 
        Opcion_1 = Button (raiz_rol, text= "Profesor", command= lambda: (filtrar_rol.set ("Profesor"), try_rol ()))
        Opcion_1.grid (row= 1, column=0)

        Opcion_2 = Button (raiz_rol, text= "Estudiante", command= lambda: (filtrar_rol.set ("Estudiante"), try_rol ()))
        Opcion_2.grid (row= 1, column= 1)
  
# Esta funcion es similar a la que esta en la de "Search users", en este caso seria lo mismo que mostrar, pero para modificar datos
    def mod_data():
        modificable = User_entry.get() #Aqui se declara la variable antes de usarse para que no ocurran errores
        try:
            if modificable == "":
                mod_dat.set ("Debe ingresar un nombre de usuario")
                restore_mod = Button (mod_options,text="Restaurar", command= lambda: (mod_dat.set (""), restore_mod.destroy()))
                restore_mod.grid (row=3, column=0)
            else:
                if connections.read (modificable) == True:
                    mod_dat.set(f"¿Que información desea modificar del usuario?:  | {modificable} |")
                    del_moder= Button (mod_options, text= "Terminar y cerrar ventana de modificaciones", width= 35, command= lambda: mod_raiz.destroy())
                    del_moder.grid (row=3, column=0)

                    #nombre_de_usuario = Button(mod_options, text= "Cambiar nombre de usuario"); nombre_de_usuario.grid (row=0, column=0)
                    edad = Button (mod_options, text= "Cambiar edad del usuario", command= mod_edad, width= 20); edad.grid (row=0, column=0)
                    sexo = Button (mod_options, text= "Cambiar sexo del usuario", command= mod_sexo, width= 20); sexo.grid (row=1, column=0)
                    rol = Button (mod_options, text= "Cambiar rol del usuario", command= mod_rol, width= 20); rol.grid (row=2, column=0)
                else:
                    mod_dat.set(f"El usuario | {modificable} | no fue encontrado o no existe")
                    restore_mod= Button (mod_options,text="Restaurar", command= lambda: (mod_dat.set (""), restore_mod.destroy()))
                    restore_mod.grid (row=3, column=0)
        except:
            #Aquí no pasa nada, solo es para cubrir el hecho de que aún 
            #no encuentro excepciones ¯/_(ツ)_/¯
            pass
    
    #Boton para hacer modificaciones al usuario, que obligatoria
    Loged_us =  Button (mod_frame, text= "Buscar usuario", command= mod_data)
    Loged_us.grid (row= 1, column=1)

    mod_raiz.mainloop ()

#Función para borrar usuarios
def del_users ():
    try:
        from VIEW_Calculadora_basica import raiz
        raiz.withdraw ()
        try:
            from VIEW_cal_grafica import raiz as graf
            graf.withdraw ()
        except:
            pass
    except:
        pass

    def del_verificate():
        try:
            borrable = del_entry.get ()
            Pword_comprobation = Pword_entry.get ()
            if borrable == "" or Pword_comprobation == "":
                no_user_var.set ("Debe ingresar un nombre de usuario y contraseña para poder borrarlo")           
            
            elif connections.read (borrable) == True and borrable == connections.acceso_usuarios (borrable, Pword_comprobation):
                final_delete = messagebox.askyesno (title= "Advertencia", message= "¿Desea continuar?, tenga en cuenta que su usuario será borrado para siempre")

                if final_delete != False:
                    # Aqui se utiliza la función para borrar del model llamada "delete"
                    # cuando el usuario ha aceptado eliminar su usuario
                    connections.delete (borrable) 

                    deleted_user = Label(delU_raiz, text= "El usuario se ha eliminado correctamente", font= (None, 14),padx= 460, pady=100)
                    deleted_user.place (relx= 0.5, rely= 0.4, anchor= "center")

                    end_del_us = Button (delU_raiz, text= "Cerrar ventana para borrar usuarios", command= lambda: (delU_raiz.destroy(), forzar_ventana_de_inicio ()))
                    end_del_us.place (relx= 0.5, rely= 0.7, anchor= "center")
                    
                    def forzar_ventana_de_inicio ():
                        try:
                            import VIEW_Ventana_de_inicio as vp
                            from main import iniciar

                            vp.root_prueba.destroy ()
                            iniciar ()

                        except ImportError:
                            pass # En caso de que npo pueda importar alguna de las funciones
                else:
                    pass
            else:
                raise Exception
        except:
                no_user_var.set ("El usuario que ingreso no esta registrado en la base de datos")

    delU_raiz = Toplevel ()
    delU_raiz.title ("Eliminar usuarios")
    delU_raiz.geometry ("478x150")
    delU_raiz.resizable (False, False)

    #Label de instruccion
    delete_label = Label (delU_raiz, text= "Ingrese el nombre de usuario que desea eliminar\ny su contraseña", font= (None, 16))
    delete_label.grid (row= 0, column= 0, columnspan= 2)

    #Label para mostrar si la entrada esta vacia
    no_user_var = StringVar ()
    no_user = Label (delU_raiz, textvariable= no_user_var)
    no_user.grid (row= 3, column=0, columnspan= 2)
    
    # Label usuario
    label_usuario = Label (delU_raiz, text= "Usuario", width= 10)
    label_usuario.grid (row= 1, column= 0)
    
    # Label contraseña
    label_contraseña = Label (delU_raiz, text= "Contraseña", width= 10)
    label_contraseña.grid (row= 2, column= 0)
    
    #Entrada para ingresar el usuario
    del_entry = Entry (delU_raiz, width= 40)
    del_entry.grid (row= 1, column= 1)
    
    # Entrada para contraseña
    Pword_entry =Entry (delU_raiz, width= 40)
    Pword_entry.grid (row= 2, column= 1)

    #Boton de enviar
    del_enviar = Button (delU_raiz, text= "Eliminar usuario", command= del_verificate)
    del_enviar.grid (row= 4, column= 0, columnspan= 2)

    def Abort_delete ():
        try:
            from VIEW_Calculadora_basica import raiz
            delU_raiz.destroy ()
            raiz.deiconify ()
        except:
            pass
        
        try:
            from VIEW_cal_grafica import raiz as graf
            delU_raiz.destroy ()
            graf.deiconify ()
        except:
            pass
    delU_raiz.protocol ("WM_DELETE_WINDOW", Abort_delete)