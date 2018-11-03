import pygame

def rec_in_frame():
	""" Con esta funcion vamos a crear un Frame que tenga
	un titulo, color de fondo y un rectangulo"""
	
	# Inicializamos Pygame
	pygame.init()

	# Creamos superficie de la ventana en la que trabajaremos(ancho, largo)
	Frame = pygame.display.set_mode((600, 600))

	# Titulo de la ventana
	pygame.display.set_caption("¿Como hacer un rectangulo en Pygame?")

	# Creamos un cuadrado  (posicion_x, posicion_y, ancho, largo)
	rect = (100, 100, 150, 100)

	# El color (RED,GREEN,BLUE)
	color = (255, 0, 100)
	
	#  El cliclo del Frame
	while True:
		# Busca los eventos posibles (teclado, mouse, etc)
		ev = pygame.event.poll()
		
		# Permite que al oprimir el boton de cerrar la venta salga del loop del while
		if ev.type == pygame.QUIT:
			break
			
		# Color de la ventana (R, G, B)
		Frame.fill((0, 200, 255))

		# Dibuja sobre la ventana (de algun color, un objeto)
		Frame.fill(color, rect)
		
		# La superficie esta lista, 
		pygame.display.flip()
		
	# Cerrar la ventana
	pygame.quit()

# Inicializamos la funcion
rec_in_frame()
