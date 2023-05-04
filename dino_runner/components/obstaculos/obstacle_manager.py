import pygame
import random
from dino_runner.components.cactus import Cactus
from dino_runner.components.cactus import Cactus2
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            cactus2 = Cactus2 (LARGE_CACTUS)
            bird = Bird (BIRD)
            obstacle_type = random.choice(["small", "large", "bird"])
            if obstacle_type == "small":
                self.obstacles.append(cactus)

            if obstacle_type == "large":
                self.obstacles.append(cactus2)

            if obstacle_type == "bird":
                self.obstacles.append(bird)

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
