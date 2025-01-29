import pygame,sys,random
from raycasting import *

BLACK = (0,0,0)
WIDTH,HEIGHT = 750,750
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def update(particle,boundaries):
	WINDOW.fill(BLACK)
	for wall in boundaries:
		wall.update(WINDOW)
	particle.look(boundaries,WINDOW)
	particle.update()
	pygame.display.update()

def main(boundary_num=5):
	boundaries = [Boundary([random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)],[random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)]) for i in range(boundary_num)]
	particle = Particle(WIDTH,HEIGHT)
	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		update(particle,boundaries)

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 1:
		main()
	elif len(args) == 2:
		if args[1].isdigit():
			main(int(args[1]))
		else:
			print("Boundary Number must be an Integer!")
			print("Usage: python main.py <Boundary Number>")
	else:
		print("Usage: python main.py <Boundary Number>")