import turtle
# "turtle" es una libreria grafica que incluye python, para mas
# informacion consultar la documentacion en el siguiente link...
# "https://docs.python.org/3.3/library/turtle.html?highlight=turtle"

# Creamos la ventana en la que trabajaremos con dimensiones (ancho, alto)
turtle.setup(400, 500)
# Declaramos la ventana como un objeto de tipo "Screen"
window = turtle.Screen()
# Le ponemos un titulo a la ventana
window.title("Keypresses Events!")
# Definimos el color de fondo de la ventana
window.bgcolor("lightgreen")

# Declaramos un objeto de tipo "Turtle"
goku = turtle.Turtle()

# Definimos nuestros "Keypresses Events"

# La tortuga se mueve 30 pixeles hacia donde este apuntando
def mover(): goku.forward(30)
# La tortuga gira 45° a la izquierda
def girarIzq(): goku.left(45)
# La tortuga gira 45° a la derecha
def girarDer(): goku.right(45)
# Cerrar la ventana
def salir(): window.bye()

# Asociamos cada "Keypress Event" con una tecla determinada
# Sintaxis: "ventana".onkey("Keypress Event", "tecla")

# Asociamos el evento mover con la tecla "arriba"
window.onkey(mover, "Up")
# Asociamos el evento girarIzq con la tecla "izquierda"
window.onkey(girarIzq, "Left")
# Asociamos el evento girarDer con la tecla "derecha"
window.onkey(girarDer, "Right")
# Asociamos el evento salir con la tecla "q" en minuscula
window.onkey(salir, "q")

# Siempre que se ejecuten "Keypresses Events", se debe usar
# el comando "ventana".listen() para enlazar los eventos con
# lo que ocurre en la ventana, de otro modo no se ejecutaran
window.listen()

# "ventana".mainloop() hace que la ventana se mantenga abierta
window.mainloop()
