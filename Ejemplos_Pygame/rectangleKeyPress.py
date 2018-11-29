import pygame

# Inicializamos el programa
pygame.init()

# Llamamos a nuestra ventana (tamaño_x, tamaño_y)
ventana = pygame.display.set_mode((500, 500))

# Le ponemos un titulo a nuestra ventana
pygame.display.set_caption("Movimientos en Pygame")

# Vamos a crear las caracteristicas para un rectangulo
x = 50
y = 50
ancho = 40
alto = 60

# Velocidad en la que se va a desplazar nuestro rectangulo
vel = 5

estado = True
while estado:
	# Velocidad del programa en milisegundos
	pygame.time.delay(100)

	# Atrapa todos los posibles eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			estado = False

	keys = pygame.key.get_pressed()
	# Al accionar las flechas del teclado el rectangulo se desplaza a...
	# ... esa direccion
	if keys[pygame.K_LEFT]:
		x -= vel
	if keys[pygame.K_RIGHT]:
		x += vel
	if keys[pygame.K_UP]:
		y -= vel
	if keys[pygame.K_DOWN]:
		y += vel

	# Rellenar el fondo de la ventana con cada movimiento del rectangulo
	ventana.fill((0,0,0))

	# Creamos nuestro rectangulo con las especificaciones ya dadas
	pygame.draw.rect(ventana, (255, 0, 0), (x, y, ancho, alto))

	# Muestra lo que esta en la pantalla
	pygame.display.flip()

# Cierra la ventana
pygame.quit()
