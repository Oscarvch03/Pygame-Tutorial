import pygame

def image_in_frame():
	"""Con esta funcion vamos a crear un Frame que tenga
	titulo, color de fondo y una imagen"""
		
	# Inicializamos Pygame
	pygame.init()

	# Creamos superficie de la ventana en la que trabajaremos(ancho, largo)
	Frame = pygame.display.set_mode((600, 600))

	# Titulo de la ventana
	pygame.display.set_caption("¿Una imagen en Pygame?")

	# Vamos a crear un objeto con una imagen
	"download picture from: https://www.pexels.com/search/celebration/"
	# Asegurese de guardar la imagen en el mismo...
	# ...directorio donde esta el scrip
	image = pygame.image.load("yeah.jpeg")

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

		# Sube la imagen a la ventana (objeto,(posicion_x, posicion_y))
		Frame.blit(image, (50,100))

		# La superficie esta lista, 
		pygame.display.flip()
		
	# Cerrar la ventana
	pygame.quit()

# Inicializar el programa
image_in_frame()
