from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius -  ASTEROID_MIN_RADIUS)
        asteroid_1.velocity = 1.2 * self.velocity.rotate(random_angle)

        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius -  ASTEROID_MIN_RADIUS)
        asteroid_2.velocity = 2.0 * self.velocity.rotate(-random_angle)
