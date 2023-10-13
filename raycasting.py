import pygame,sys,math,random

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class Boundary:
	def __init__(self,pos1,pos2):
		self.a = pos1
		self.b = pos2

	def update(self,window):
		pygame.draw.line(window,WHITE,self.a,self.b)

class Ray:
	def __init__(self,pos,angle):
		self.pos = pos
		self.dir = [10*math.cos(angle),10*math.sin(angle)]

	def lookAt(self,x,y):
		self.dir[0] = x - self.pos[0]
		self.dir[1] = y - self.pos[1]

	def cast(self,boundary):
		den = (boundary.a[0]-boundary.b[0])*(self.pos[1]-(self.pos[1]+self.dir[1]))-(boundary.a[1]-boundary.b[1])*(self.pos[0]-(self.pos[0] + self.dir[0]))
		#     (x1 - x2)*(y3-y4) - (y1-y2)*(x3-x4)
		if den == 0:
			return False
		t = ((boundary.a[0]-self.pos[0])*(self.pos[1]-(self.pos[1] + self.dir[1]))-(boundary.a[1]-self.pos[1])*(self.pos[0]-(self.pos[0]+self.dir[0])))/den
		#   (x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)
		u = -((boundary.a[0]-self.pos[0])*(boundary.a[1]-boundary.b[1])-(boundary.a[1]-self.pos[1])*(boundary.a[0]-boundary.b[0]))/den
		#   (x1-x3)*(y1-y2) - (y1-y3)*(x1-x2)
		if t > 0 and t < 1 and u > 0:
			pt = [0,0]
			pt[0] = boundary.a[0] + t*(boundary.b[0] - boundary.a[0])
			pt[1] = boundary.a[1] + t*(boundary.b[1] - boundary.a[1])
			return pt
		else:
			return False

class Particle:
	def __init__(self,WIDTH,HEIGHT):
		self.pos = [WIDTH/2,HEIGHT/2]
		self.rays = []
		for i in range(36):
			self.rays.append(Ray(self.pos,math.radians(i*10)))

	def look(self,walls,window):
		for ray in self.rays:
			closest = None
			record = 10000000000000
			for wall in walls:
				pt = ray.cast(wall)
				if pt:
					d = ((self.pos[0] - pt[0])**2 + (self.pos[1] - pt[1])**2)**0.5
					if d <= record:
						record = d
						closest = pt
			if closest:
				pygame.draw.line(window,WHITE,[self.pos[0],self.pos[1]],[closest[0],closest[1]])

	def update(self):
		self.pos[0],self.pos[1] = pygame.mouse.get_pos()
		rect = pygame.Rect(self.pos[0],self.pos[1],25,25)