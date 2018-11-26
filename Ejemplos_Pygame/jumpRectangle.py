import pygame

def jumpRectangle():
	"""Vamos a Crear una funcion que cree un rectangulo, el cual se
	pueda desplazar al presionar las flechas izq y der del teclado y
	salte con la barra espaciadora"""

	# Inicializamos el programa
	pygame.init()

	# Llamamos una variable para definir el tamaño de nuestra ventana
	# Y llamamos una variable para invocar el Frame
	ven_sz = 500
	ventana = pygame.display.set_mode((ven_sz, ven_sz))

	# Le ponemos un titulo a nuestra ventana
	pygame.display.set_caption("Movimientos en Pygame")

	# Vamos a crear las caracteristicas para nuestro rectangulo
	x = 100
	y = 400
	ancho = 40
	alto = 60

	# La velocidad en la que se va a desplazar
	vel = 5

	# Declaramos unas variables que luego nos ayudaran con el salto del...
	# ...rectangulo
	isJump = False
	jumpCount = 10

	# Una variable para luego poder cerrar el mainloop
	estado = True
	# Mainloop
	while estado:

		# Velocidad del programa en milisegs
		pygame.time.delay(100)

		# Atrapa todos los posibles eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				estado = False

		keys = pygame.key.get_pressed()

		# Al accionar las teclas del teclado el rectangulo se desplazara de...
		# ...lateralmente
		if keys[pygame.K_LEFT] and x  > 0:
			x -= vel
		if keys[pygame.K_RIGHT] and x < (ven_sz - ancho):
			x += vel
		# En este condicional buscamos que en el momento en  el rectangulo...
		# ... este saltando no se pueda mover verticalmente o vuelva a saltar
		if not (isJump):
			if keys[pygame.K_UP] and y > 0:
				y -= vel
			if keys[pygame.K_DOWN] and y < (ven_sz - alto):
				y += vel
			if keys[pygame.K_SPACE]:
				isJump = True

		# Con esta funcion logramos que el rectangulo al presionar la tecla...
		# ... ESPACIO se desplace hacia arriba y vaya desacelerando hasta...
		# ... llegar al punto maximo luego de esto empiece a descender...
		# ... acelerando hasta volver a su posicion inicial

		else:
			if jumpCount  >= -10:
				neg = 1
				if jumpCount < 0:
					neg = -1
				y -= ( jumpCount ** 2) * 0.5 * neg
				jumpCount -= 1
			else:
				isJump = False
				jumpCount = 10


		# Rellenar el fondo de la ventana con cada movimiento del rectangulo
		ventana.fill((0, 0, 0))

		# Creamos nuestro rectangulo con las especificaciones ya dadas
		pygame.draw.rect(ventana, (255, 0, 0), (x, y, ancho, alto))

		# Muestra lo que esta en la pantalla
		pygame.display.flip()

	# Cierra la ventana
	pygame.quit()
jumpRectangle()
