# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from scoresprite import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    image_drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    ScoreSprite.containers = (updatable, drawable,image_drawable)

    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (asteroidfield, updatable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable,drawable)

    score = ScoreSprite(20, 20)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        dt = clock.tick(60) / 1000
        player.cool_down -= dt
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid) == False:
                print("Game Over!")
                print(f"score : {score.score}")
                return
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid) == False:
                    score.set_score(score.score + asteroid.radius)
                    asteroid.split()
                    shot.kill()
                

        screen.fill("black")


        image_drawable.draw(screen)
#        drawable.draw(screen)

        for thing in drawable:
           thing.draw(screen)
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
