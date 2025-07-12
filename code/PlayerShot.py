from code.Const import entity_speed
from code.entity import Entity


class PlayerShot(Entity):

    def __inity__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx += entity_speed[self.name]
