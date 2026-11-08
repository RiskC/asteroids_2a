import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	#game loop
	while True:
		log_state()
		#event queue
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		#fill screen with black to wipe away anything from last frame
		screen.fill("black")

		#draw player
		player.draw(screen)
		player.update(dt)


		#refresh screen
		pygame.display.flip()

		#fps
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
