from locale import D_T_FMT
from logger import log_event
import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ran_angle = random.uniform(20,50)
        a1_vector = self.velocity.rotate(ran_angle)
        a2_vector = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position, self.position, new_radius)
        ast2 = Asteroid(self.position, self.position, new_radius)
        ast1.velocity = a1_vector * 1.2
        ast2.velocity = a2_vector * 1.2
