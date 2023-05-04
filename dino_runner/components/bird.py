import pygame
import random
from dino_runner.components.obstaculos.obstacle import Obstacle

class Bird(Obstacle):
   niveles = [170, 220, 260]
   def __init__(self, image):
      self.step_index = 0 
      self.Y_POS = self.niveles
      self.type = 0
      super().__init__(image, self.type)
      self.rect.y = random.choice(self.Y_POS)


   def draw(self, screen):
      if self.step_index >= 9:
         self.step_index = 0
      screen.blit(self.image[self.step_index // 5], self.rect)
      self.step_index += 1


