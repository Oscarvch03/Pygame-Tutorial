import pygame

pygame.init()

ancho_vn = 556
alto_vn = 755

ventana = pygame.display.set_mode((ancho_vn,alto_vn))

pygame.display.set_caption("Pacman")

DERECHA = [pygame.image.load('pc_r.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_r.png'), pygame.image.load('pc_r.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_r.png'), pygame.image.load('pc_r.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_r.png')]
IZQUIERDA = [pygame.image.load('pc_l.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_l.png'), pygame.image.load('pc_l.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_l.png'), pygame.image.load('pc_l.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_l.png')]
ARRIBA = [pygame.image.load('pc_u.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_u.png'), pygame.image.load('pc_u.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_u.png'), pygame.image.load('pc_u.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_u.png')]
ABAJO = [pygame.image.load('pc_d.png'),  pygame.image.load('pc_c.gif'), pygame.image.load('pc_d.png'), pygame.image.load('pc_d.png'),  pygame.image.load('pc_c.gif'),pygame.image.load('pc_d.png'), pygame.image.load('pc_d.png'), pygame.image.load('pc_c.gif'),   pygame.image.load('pc_d.png')]

quieto = pygame.image.load('pc_c.gif')
fondo = pygame.image.load("bg_pcman.jpg")

class player():
	def __init__(self, x, y, ancho, alto):
		self.x = x
		self.y = y
		self.ancho = ancho
		self.alto = alto
		self.vel = 5
		self.izq = False
		self.der = False
		self.arr = False
		self.ab = False
		self.walkCount = 0
	
	def draw(self, ventana):
		if self.walkCount +1 >= 27:
			self.walkCount = 0
		if self.izq:
			ventana.blit(IZQUIERDA[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
		elif self.der:
			ventana.blit(DERECHA[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
		elif self.arr:
			ventana.blit(ARRIBA[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
		elif self.ab:
			ventana.blit(ABAJO[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1
		else:
			ventana.blit(quieto, (self.x,self.y))



def dibujar():

	ventana.blit(fondo, (0,0))
	pcman.draw(ventana)
	pygame.display.update()

estado = True

pcman = player(300, 410, 32, 32)
while estado:
	pygame.time.delay(27)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			estado = False


	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and pcman.x > 15:
		pcman.x -= pcman.vel
		pcman.izq = True
		pcman.der = False
		pcman.arr = False
		pcman.ab = False
	
	elif keys[pygame.K_RIGHT] and pcman.x < (ancho_vn - pcman.ancho -10) :
		pcman.x +=pcman. vel
		pcman.izq = False
		pcman.der = True
		pcman.arr = False
		pcman.ab = False
		
	elif keys[pygame.K_UP] and pcman.y > 15:
		pcman.y -= pcman.vel
		pcman.izq = False
		pcman.der = False
		pcman.arr = True
		pcman.ab = False
		
	elif keys[pygame.K_DOWN] and pcman.y < (alto_vn- pcman.alto-15):
		pcman.y += pcman.vel
		pcman.izq = False
		pcman.der = False
		pcman.arr = False
		pcman.ab = True
	else:
		pcman.izq = False
		pcman.der = False
		pcman.arr = False
		pcman.ab = False
		pcman.walkCount =0
		
	dibujar()
	
pygame.quit()