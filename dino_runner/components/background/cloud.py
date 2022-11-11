import random
from dino_runner.components.background.background import Background

class Cloud(Background):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(50, 250)

