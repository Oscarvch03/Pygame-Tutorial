import turtle
# "turtle" es una libreria grafica que incluye python, para mas
# informacion consultar la documentacion en el siguiente link...
# "https://docs.python.org/3.3/library/turtle.html?highlight=turtle"

# Creamos la ventana en la que trabajaremos con dimensiones (ancho, alto)
turtle.setup(400, 500)
# Declaramos la ventana como un objeto de tipo "Screen"
window = turtle.Screen()
# Le ponemos un titulo a la ventana
window.title("Timer Events!")
# Definimos el color de fondo de la ventana
window.bgcolor("lightgreen")

# Declaramos un objeto de tipo "Turtle"
goku = turtle.Turtle()
# Definimos el color para la tortuga
goku.color("purple")

# Definir una funcion para que la tortuga haga un cuadrado con
# tamaño de lado 10
def cuadrado():
    for i in range(4):
        goku.forward(10)
        goku.left(90)
        goku.forward(15)

# Ejecutar la funcion "cuadrado" 2000 milisegundos despues de que se
# haya abierto la ventana
window.ontimer(cuadrado, 2000)

# "ventana".mainloop() hace que la ventana se mantenga abierta
window.mainloop()
