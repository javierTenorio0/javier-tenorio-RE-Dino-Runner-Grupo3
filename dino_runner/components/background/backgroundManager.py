import pygame
import random
from dino_runner.components.background.cloud import Cloud
from dino_runner.utils.constants import (CLOUD)

class BackgroundManager:
    def __init__(self):
        self.clouds = []
    
    def update(self, game):
        if len(self.clouds) == 0:
            clouds_bool = random.randint(0, 5)
            if clouds_bool == 0:
                self.clouds.append(Cloud(CLOUD))
        
        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)       

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen) 
    
    def reset_clouds(self, self1):
        self.clouds = []