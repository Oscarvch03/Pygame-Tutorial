import pygame

def text_in_frame():
	"""Con esta funcion vamos a crear un Frame que tenga
	titulo, color de fondo y un texto."""
	
	# Inicializamos Pygame
	pygame.init()

	# Creamos superficie de la ventana en la que trabajaremos(ancho, largo)
	Frame = pygame.display.set_mode((600, 600))

	# Titulo de la ventana
	pygame.display.set_caption("Voy a escribir en Pygame!")

	# Vamos a crear un objeto con un tipo fuente para escribir ("fuente", tamaño)
	fuente = pygame.font.SysFont("Courier", 25)

	# El cliclo del programa
	while True:
		# Busca los eventos posibles
		ev = pygame.event.poll()
		
		# Permite que al oprimir el boton de cerrar la venta...
		# ...deje de correr el programa
		if ev.type == pygame.QUIT:
			break
			
		# Color de la ventana (R, G, B)
		Frame.fill((0, 200, 255))

		# Creamos un objeto que imprimira ("un texto", bordes suaves, color)
		texto = fuente.render("¿Como escribir con Pygame?", True, (0,0,0))
		
		# Dibuja en la ventana (el texto, (posicion_x, posicion_y))
		Frame.blit(texto, (100,10))
		
		# La superficie esta lista
		pygame.display.flip()
		
	# Cerrar la ventana
	pygame.quit()

# Invocamos la funcion
text_in_frame()
