import pygame
from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            # pygame.time.delay(100)
            # print(game.player.dino_rect.colliderect(obstacle.rect))
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                self.death += 1
                break


    def draw(self, screen):
        for obstacles in self.obstacles:
            obstacles.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
