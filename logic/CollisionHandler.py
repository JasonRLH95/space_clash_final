

class CollisionHandler:
    # Checks the collision between the player and the meteors
    @staticmethod
    def check_player_enemy_collision(player, meteors):
        for meteor in meteors:
            if player.collides_with(meteor):
                return True
        return False

    # Checks collision between two instances from type Entity
    @staticmethod
    def check_entity_collision(entity1, entity2):
        return entity1.collides_with(entity2)
