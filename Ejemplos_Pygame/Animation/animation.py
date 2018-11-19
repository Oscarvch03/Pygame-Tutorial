import pygame

"En el programa animation.py vamos a crear con una serie de imagenes una animación de un personaje en Pygame."
# Inicializamos pygame
pygame.init()

# Creamos nuestra ventana 
ventana = pygame.display.set_mode((500,480))

# Titulo de la ventana
pygame.display.set_caption("Animacion en Pygame")

#Vamos a crear dos listas, una que tenga los movimientos hacia la izquierda y la otra hacia la derecha, los elementos de esta lista son Sprites.  

# Cuando se mueva a la Derecha
Derecha = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

# Y cuando se mueva a la Izquierda
Izquierda = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

# Cuando el personaje no se este desplazando lateralmente  se vera de frente
Frente = pygame.image.load('standing.png')

# Fondo de nuestro Frame
Fondo = pygame.image.load('bg.jpg')


clock = pygame.time.Clock()

# La posicion de nuestro personaje en la ventana
x = 50
y = 400

 # El tamaño de nuestro personaje
ancho = 64
alto = 64

# La velocidad con la que se desplazara
vel = 5

# Propiedades del salto
isJump = False
jumpCount = 10

# Propiedades del desplazamiento
Izq = False
Der = False
walkCount = 0


def dibujar():
	""" Esta es la funcion que va a "dibujar" lo que se va a mostrar en el Frame"""
	# Volvemos la variable walkCount a una variable global 
	global walkCount
	
	# Fondo de la animacion (variable_de_la_imagen_del_fondo(posicion_x, posicion_y))
	ventana.blit(Fondo, (0,0))
	
	# Vamos a hacer que cada "posicion" del proceso de desplazamiento dure 3 loops, al ser 9 posiciones son 27 el numero loops que hara para generar la animacion de un paso 
	if walkCount + 1 >= 27:
		walkCount = 0
	# Si se desplaza a la izquierda va a reproducir las imagenes de nuestra lista walkLeft
	if Izq:
		ventana.blit(Izquierda[walkCount//3], (x,y))
		walkCount += 1
	# Si se desplaza a la derecha va a reproducir las imagenes de nuestra lista walkRight
	elif Der:
		ventana.blit(Derecha[walkCount//3], (x,y))
		walkCount +=1
	# Si no se esta desplazando se vera la imagen de frente
	else:
		 ventana.blit(Frente, (x,y))
	# Muestra lo que esta en la pantalla
	pygame.display.update()


# Main loop
estado = True
while estado:
	# Velocidad del programa 
	clock.tick(27)

	# Atrapa todos los posibles eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			estado = False

	keys = pygame.key.get_pressed()
	# Al accionar las teclas del teclado el personaje se desplazara a la izquierda
	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		Izq = True
		Der = False
	# Al accionar las teclas del teclado el personaje se desplazara a la derecha
	elif keys[pygame.K_RIGHT] and x < 500 - ancho - vel:
		x += vel
		Der = True
		Izq = False
	else:
		Der = False
		Izq = False
		walkCount = 0
		
	# En este condicional buscamos que en el momento en  el personaje  este saltando...
	# ...y no se desplaze lateralmente se vera la imagen de frente
	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True
			Der = False
			Izq = False
			walkCount = 0
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10
	# Dibujara lo que se va a mostrar en el Frame
	dibujar()

pygame.quit()