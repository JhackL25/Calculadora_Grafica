
def cal_graf():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import TextBox, Button
    import MODEL_grafica as mod


    Historial = ['','','','']

    def update(val):
        func = function_box.text    
        update_historial(func)
        func = mod.correc_ecuacion(func)
        try:
            
            x_vals = np.linspace(-500, 500, 10000)
            y_vals = [eval(func) for x in x_vals]
            line.set_ydata(y_vals)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw_idle()
            
        except Exception as e:
            print(f"Error: {e}")

        update_historial(func)

        


    def update_historial(func):
        for i in range(len(Historial)):
            Historial[i] = Historial[i - 1]
        Historial[0] = func

    # Crear la figura y los ejes

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-10, 10)    
    ax.set_ylim(-10, 10)
    plt.subplots_adjust(0.05,0.05,0.6,0.71)
    ax.grid(which = "major", linewidth = 1)
    ax.grid(which = "minor", linewidth = 0.2)
    ax.minorticks_on()

    # Grafico inicial
    x = np.linspace(-500, 500, 10000)
    y = 2 * x**2 + 3 * x + 1
    line, = ax.plot(x, y)

    # TextBox para ingresar la función
    function_box = TextBox(plt.axes([0.15, 0.91, 0.395, 0.05]), 'Ingrese función: Y= ')
    function_box.on_submit(update)

    #Botones

    ##Potencia
    def exponente(event):
        function_box.set_val(function_box.text + "**")

    button_ax = plt.axes([0.15, 0.85, 0.095, 0.05])
    button = Button(button_ax, 'Potencia: ^')
    button.on_clicked(exponente)

    #TRIGONOMETRIAS
    ##Seno    
    def seno(event):
        function_box.set_val(function_box.text + 'sin()')

    button_ax2 = plt.axes([0.25, 0.85, 0.095, 0.05])
    button2 = Button(button_ax2, 'Sin')
    button2.on_clicked(seno)
    ##Coseno
    def coseno(event):
        function_box.set_val(function_box.text + 'cos()')

    button_ax3 = plt.axes([0.35, 0.85, 0.095, 0.05])
    button3 = Button(button_ax3, 'Cos')
    button3.on_clicked(coseno)
    ##Tangente
    def tangente(event):
        function_box.set_val(function_box.text + 'tan()')

    button_ax4 = plt.axes([0.45, 0.85, 0.095, 0.05])
    button4 = Button(button_ax4, 'Tan')
    button4.on_clicked(tangente)
    ##Cosecante
    def cosecante(event):
        function_box.set_val(function_box.text + 'csc()')
    button_ax5 = plt.axes([0.25, 0.79, 0.095, 0.05])
    button5 = Button(button_ax5, 'CSC')
    button5.on_clicked(cosecante)
    ##Secante
    def secante(event):
        function_box.set_val(function_box.text + 'sec()')

    button_ax6 = plt.axes([0.35, 0.79, 0.095, 0.05])
    button6 = Button(button_ax6, 'SEC')
    button6.on_clicked(secante)
    ##Cotrangente
    def cotangente(event):
        function_box.set_val(function_box.text + 'ctn()')

    button_ax7 = plt.axes([0.45, 0.79, 0.095, 0.05])
    button7 = Button(button_ax7, 'CTAN')
    button7.on_clicked(cotangente)
    ## Pi
    def pi(event):
        function_box.set_val(function_box.text +'π')

    button_ax9 = plt.axes([0.15, 0.79, 0.095, 0.05])
    button9 = Button(button_ax9, 'π')
    button9.on_clicked(pi)    
        

    #Historial
    Historial = ['','','','']
    ##Botones historial
    ##Boton 1
    def historial_click1(event):
        funcion_hist_correc = Historial[0]
        Historial_1 = mod.correc_historial(funcion_hist_correc)
        function_box.set_val("")  # Borra el contenido de la caja de texto
        function_box.set_val(Historial_1)  # Agrega el elemento del historial
        print(Historial_1)

    button_H1 = plt.axes([0.61, 0.66, 0.3, 0.03])
    button_H1 = Button(button_H1, Historial[0])
    button_H1.on_clicked(historial_click1)
    
    #Boton 2
    def historial_click2(event):
        funcion_hist_correc = Historial[1]
        Historial_2 = mod.correc_historial(funcion_hist_correc)
        function_box.set_val("")  # Borra el contenido de la caja de texto
        function_box.set_val(Historial_2)  # Agrega el elemento del historial
        print(Historial_2)

    button_H2 = plt.axes([0.61, 0.60, 0.3, 0.03])
    button_H2 = Button(button_H2, Historial[1])
    button_H2.on_clicked(historial_click2)

    #Boton 3
    def historial_click3(event):
        funcion_hist_correc = Historial[2]
        Historial_3 = mod.correc_historial(funcion_hist_correc)
        function_box.set_val("")  # Borra el contenido de la caja de texto
        function_box.set_val(Historial_3)  # Agrega el elemento del historial
        print(Historial_3)

    button_H3 = plt.axes([0.61, 0.54, 0.3, 0.03])
    button_H3 = Button(button_H3, Historial[2])
    button_H3.on_clicked(historial_click3)

    #Boton 4
    def historial_click4(event):
        funcion_hist_correc = Historial[3]
        Historial_4 = mod.correc_historial(funcion_hist_correc)
        function_box.set_val("")  # Borra el contenido de la caja de texto
        function_box.set_val(Historial_4)  # Agrega el elemento del historial
        print(Historial_4)

    button_H4 = plt.axes([0.61, 0.48, 0.3, 0.03])
    button_H4 = Button(button_H4, Historial[3])
    button_H4.on_clicked(historial_click4)

    # variable para cerrar la grafica    
    variable_de_control = False

    def restaurar_basica(event):
        import VIEW_Calculadora_basica as basic
        plt.close ()
        basic.raiz.deiconify ()

    
    button_Cal = plt.axes([0.81, 0.90, 0.17, 0.06])
    button_Cal = Button(button_Cal, 'Calculadora Basica O_o')
    button_Cal.on_clicked(restaurar_basica)

    plt.show ()