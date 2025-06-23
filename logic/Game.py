
from space_clash_final_folder.space_clash_final.logic.Player import Player
from space_clash_final_folder.space_clash_final.logic.Meteor import MeteorManager
from space_clash_final_folder.space_clash_final.logic.CollisionHandler import CollisionHandler
from space_clash_final_folder.space_clash_final.logic.ScoreManager import ScoreManager
from space_clash_final_folder.space_clash_final.assets.assets import *
from space_clash_final_folder.space_clash_final.logic.Explosion import Explosion


class Game:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.is_paused = False
        self.player = Player(game_settings["spaceship"], game_settings["bullet_color"], self.is_paused)
        self.chapter_pass = False
        self.meteor_manager = MeteorManager()
        self.collision_handler = CollisionHandler()
        self.score_manager = ScoreManager()
        self.is_game_over = False
        self.explosions = []
        self.chapter_pause_timer = 0

    # Handles the game functionality
    def update(self):
        # Pause or game over events
        if self.is_paused or self.is_game_over:
            return

        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Player shoot event
        if keys[pygame.K_SPACE]:
            self.player.shoot()
            SHOOT_CHANNEL.stop()
            SHOOT_CHANNEL.play(BULLET_FIRE_SOUND)
        self.player.handle_bullets(WIN)

        # Handles meteors behavior
        self.meteor_manager.update()
        removed_meteors = self.meteor_manager.remove_off_screen()
        for _ in range(removed_meteors):
            self.score_manager.add_dodge_score()
        # Check collision between player and meteors
        if self.collision_handler.check_player_enemy_collision(self.player, self.meteor_manager.get_meteors()):
            self.is_game_over = True
            SPACE_CHANNEL.stop()
        # Check collision between meteors and bullets
        for meteor in self.meteor_manager.get_meteors()[:]:
            for bullet in self.player.bullets[:]:
                if self.collision_handler.check_entity_collision(bullet, meteor):
                    self.player.bullets.remove(bullet)
                    self.meteor_manager.meteors.remove(meteor)
                    explosion = Explosion(meteor.rect.centerx, meteor.rect.centery, EXPLOSION_IMAGE)
                    self.explosions.append(explosion)
                    self.score_manager.add_score(SCORE_PER_HIT)
                    EXPLOSION_CHANNEL.stop()
                    EXPLOSION_CHANNEL.play(BULLET_HIT_SOUND)
                    break
        # Dynamic update of explosions amount to display appear and disappear
        self.explosions[:] = [e for e in self.explosions if not e.update()]

    # Draw the game objects, background, player, etc.
    def draw(self, surface):
        WIN.blit(self.game_settings["background"], (0, 0))
        self.player.draw(surface)
        self.player.handle_bullets(surface)
        self.meteor_manager.draw(surface)
        for explosion in self.explosions:
            explosion.draw(surface)

    # Handle game music and transform pause stat
    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            SPACE_CHANNEL.pause()
        elif not self.is_paused:
            SPACE_CHANNEL.unpause()

    # Reset the game to start a new game
    def reset(self):
        SPACE_CHANNEL.play(GAME_SOUND, loops=-1)
        self.player.reset()
        self.meteor_manager.reset()
        self.score_manager.reset_score()
        self.is_paused = False
        self.is_game_over = False

    # Display the scores of current game
    def get_score(self):
        return self.score_manager.get_current_score()

    # When game over - saves the scores to have access to it at GameOverScreen
    def save_score(self, player_name):
        return self.score_manager.save_record(player_name)
