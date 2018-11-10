import turtle
# "turtle" es una libreria grafica que incluye python, para mas
# informacion consultar la documentacion en el siguiente link...
# "https://docs.python.org/3.3/library/turtle.html?highlight=turtle"

# Creamos la ventana en la que trabajaremos con dimensiones (ancho, alto)
turtle.setup(400, 500)
# Declaramos la ventana como un objeto de tipo "Screen"
window = turtle.Screen()
# Le ponemos un titulo a la ventana
window.title("Mouse Events!")
# Definimos el color de fondo de la ventana
window.bgcolor("lightgreen")

# Declaramos un objeto de tipo "Turtle"
goku = turtle.Turtle()
# Definimos un color para la tortuga
goku.color("purple")
# Definimos el grosor del lapiz de la tortuga
goku.pensize(3)
# Definimos la forma de la tortuga
goku.shape("circle")


# Definimos nuestro "Mouse Event"
# Ya que la interfaz grafica de turtle funciona como un plano cartesiano,
# al dar click en un pixel determinado la tortuga se movera alli
def mover(x, y):
    goku.goto(x, y)
    # Mostrar en el titulo la coordenada de la tortuga
    window.title("Mouse Events! " +
                 "La coordenada de la tortuga es ({0},{1})".format(x,y))

# Al dar click en la ventana se ejecutara la funcion que se enlace con
# el "Mouse Event"
# Sintaxis: "ventana".onclick("funcion")
window.onclick(mover)

# "ventana".mainloop() hace que la ventana se mantenga abierta
window.mainloop()
