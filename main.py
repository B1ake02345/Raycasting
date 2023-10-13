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

def main():
	boundaries = [Boundary([random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)],[random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)]) for i in range(5)]
	particle = Particle(WIDTH,HEIGHT)
	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		update(particle,boundaries)

if __name__ == "__main__":
	main()