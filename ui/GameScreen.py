

from space_clash_final_folder.space_clash_final.logic.Game import Game
from space_clash_final_folder.space_clash_final.assets.assets import *


class GameScreen:
    def __init__(self, screen, switch_screen, game_settings):
        self.screen = screen
        self.switch_screen = switch_screen
        self.game_settings = game_settings
        self.game = Game(game_settings)

        self.pause_button_rect = pygame.Rect(SCREEN_WIDTH - 130, 20, 110, 40)
        self.menu_button_rect = pygame.Rect(20, 20, 180, 40)

    # Handle events of pressing the pause or back to ment buttons
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.pause_button_rect.collidepoint(mouse_pos):
                self.game.toggle_pause()
            elif self.menu_button_rect.collidepoint(mouse_pos):
                SPACE_CHANNEL.stop()
                self.switch_screen(SCREEN_MENU)

    # Updating the score as long as game running, if game stops => saves current score and move to game over screen
    def update(self):
        self.game.update()

        if self.game.is_game_over:
            score_data = {"score": self.game.get_score()}
            self.switch_screen(SCREEN_GAME_OVER, score_data)

    # Handles the drawing all the objects on the screen, the game it self, the settings and so on
    def draw(self):
        self.screen.fill(WHITE)

        # Game entities
        self.game.draw(self.screen)
        self.game.game_settings = self.game_settings
        self.game.player.spaceship = self.game_settings["spaceship"]
        self.game.player.shot_color = self.game_settings["bullet_color"]

        # Score
        score = FONT_SMALL.render(f"Score: {self.game.get_score()}", True, WHITE)
        self.screen.blit(score, score.get_rect(center=(SCREEN_WIDTH // 2, 20)))

        # Pause button
        pause_text = "Continue" if self.game.is_paused else "Pause"
        mouse_pos = pygame.mouse.get_pos()
        pause_color = DARK_GRAY if self.pause_button_rect.collidepoint(mouse_pos) else GRAY
        pygame.draw.rect(self.screen, pause_color, self.pause_button_rect, border_radius=5)
        pause_label = FONT_SMALL.render(pause_text, True, BLACK)
        self.screen.blit(pause_label, pause_label.get_rect(center=self.pause_button_rect.center))

        # Menu button
        menu_color = DARK_GRAY if self.menu_button_rect.collidepoint(mouse_pos) else GRAY
        pygame.draw.rect(self.screen, menu_color, self.menu_button_rect, border_radius=5)
        menu_label = FONT_SMALL.render("Back to Menu", True, BLACK)
        self.screen.blit(menu_label, menu_label.get_rect(center=self.menu_button_rect.center))

        # Pause overlay
        if self.game.is_paused:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            self.screen.blit(overlay, (0, 0))

            paused_text = FONT_SMALL_LARGE.render("Paused", True, WHITE)
            self.screen.blit(paused_text, paused_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    # Reset the game
    def reset(self):
        self.game.reset()
