from code import enemy
from code.Const import win_width, ENTITY_SCORE
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= win_width:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                if isinstance(ent1, Enemy) and isinstance(ent2, Player):
                    ent2.health -= ent1.damage
                    ent2.last_dmg = ent1.name
                    print(f"{ent2.name} devour {ent1.damage} de dang! Vida: {ent2.health}")

                elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
                    ent1.health -= ent2.damage
                    ent1.last_dmg = ent2.name
                    print(f"{ent1.name} devour {ent2.damage} de dang! Vida: {ent1.health}")


                elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
                    ent2.health -= ent1.damage
                    ent1.health = 0
                    ent2.last_dmg = ent1.name

                elif isinstance(ent2, PlayerShot) and isinstance(ent1, Enemy):
                    ent1.health -= ent2.damage
                    ent2.health = 0
                    ent1.last_dmg = ent2.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
