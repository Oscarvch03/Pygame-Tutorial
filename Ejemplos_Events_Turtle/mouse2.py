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
# Definimos el color para la tortuga
goku.color("purple")

# Declaramos un nuevo objeto de tipo "Turtle"
gohan = turtle.Turtle()
# Definimos el color para la nueva tortuga
gohan.color("yellow")
# Bloqueamos el lapiz para que no dibuje nada en la pantalla
gohan.penup()
# Debemos desplazar nuestra nueva tortuga un poco, sino quedaria en la
# misma coordenada que la otra
gohan.forward(50)
# Desbloquemos el lapiz para poder dibujar en la pantalla
gohan.pendown()

# Definimos nuestros "Mouse Events"

# Ya que la interfaz grafica de turtle funciona como un plano cartesiano,
# al dar click en una tortuga y mantenerlo presionado mientras movemos
# el mouse a un pixel determinado la tortuga se movera alli
def mover_goku(x1, y1):
    # Mostrar en el titulo la coordenada de la primera tortuga
    window.title("Coordenada goku: ({0}, {1})".format(x1, y1))
    goku.goto(x1, y1)

def mover_gohan(x2, y2):
    # Mostrar en el titulo la coordenada de la segunda tortuga
    window.title("Coordenada gohan: ({0}, {1})".format(x2, y2))
    gohan.goto(x2, y2)

# Al dar click en la respectiva tortuga y mantenerlo presionado mientras
# movemos el mouse a un pixel determinado se ejecutara la funcion que se
# enlace con el "Mouse Event"
# Sintaxis: "tortuga".onrelease("funcion")
goku.onrelease(mover_goku)
gohan.onrelease(mover_gohan)

# "ventana".mainloop() hace que la ventana se mantenga abierta
window.mainloop()
