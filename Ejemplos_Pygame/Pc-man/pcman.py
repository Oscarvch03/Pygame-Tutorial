import pygame

pygame.init()

ancho_vn = 556
alto_vn = 755

ventana = pygame.display.set_mode((ancho_vn,alto_vn))

pygame.display.set_caption("Pacman")

DERECHA = [pygame.image.load('pc_r.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_r.png'), pygame.image.load('pc_r.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_r.png'), pygame.image.load('pc_r.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_r.png')]
IZQUIERDA = [pygame.image.load('pc_l.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_l.png'), pygame.image.load('pc_l.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_r.png'), pygame.image.load('pc_l.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_l.png')]
ARRIBA = [pygame.image.load('pc_u.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_u.png'), pygame.image.load('pc_u.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_u.png'), pygame.image.load('pc_u.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_u.png')]
ABAJO = [pygame.image.load('pc_d.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_d.png'), pygame.image.load('pc_d.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_d.png'), pygame.image.load('pc_d.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_d.png')]

quieto = pygame.image.load('pc_c.gif')
fondo = pygame.image.load("bg_pcman.jpg")

x = 15
y = 15
ancho = 32
alto = 32

vel = 5

estado = True

walkCount = 0

def dibujar():
	global walkCount
	ventana.blit(fondo, (0,0))
	
	if walkCount +1 >= 27:
		walkCount = 0
	if izq:
		ventana.blit(IZQUIERDA[walkCount//3], (x,y))
		walkCount += 1
	elif der:
		ventana.blit(DERECHA[walkCount//3], (x,y))
		walkCount += 1
	elif arr:
		ventana.blit(ARRIBA[walkCount//3], (x,y))
		walkCount += 1
	elif ab:
		ventana.blit(ABAJO[walkCount//3], (x,y))
		walkCount += 1
	else:
		ventana.blit(quieto, (x,y))

	pygame.display.update()

while estado:
	pygame.time.delay(27)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			estado = False


	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 15:
		x -= vel
		izq = True
		der = False
		arr = False
		ab = False
	
	elif keys[pygame.K_RIGHT] and x < (ancho_vn - ancho -10) :
		x += vel
		izq = False
		der = True
		arr = False
		ab = False
		
	elif keys[pygame.K_UP] and y > 15:
		y -= vel
		izq = False
		der = False
		arr = True
		ab = False
		
	elif keys[pygame.K_DOWN] and y < (alto_vn- alto-15):
		y += vel
		izq = False
		der = False
		arr = False
		ab = True
	else:
		izq = False
		der = False
		arr = False
		ab = False
		walkCount =0
		
	dibujar()
	
pygame.quit()