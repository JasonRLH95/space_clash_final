

import sys
from p2.ui.ChoosePlayerScreen import ChoosePlayerScreen
from p2.ui.GameScreen import GameScreen
from p2.ui.GameOverScreen import GameOverScreen
from p2.ui.HighScoresScreen import HighScoresScreen
from p2.assets.assets import *


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_settings = {
            "background": SPACE_1,
            "spaceship": WHITE_SPACESHIP,
            "bullet_color": BLUE
        }

        # Current state
        self.current_screen = "menu"
        self.screen_data = {}

        # UI: menu buttons
        self.new_game_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 250, 300, 60)
        self.high_scores_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 330, 300, 60)
        self.quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 410, 300, 60)

        # Screens
        self.choose_player_screen = ChoosePlayerScreen(self.screen, self.switch_screen)
        self.game_screen = GameScreen(self.screen, self.switch_screen, self.game_settings)
        self.game_over_screen = GameOverScreen(self.screen, self.switch_screen)
        self.high_scores_screen = HighScoresScreen(self.screen, self.switch_screen)

        self.run()

    # Handles the switching between the screens and transfer the data between the pages
    def switch_screen(self, screen_name, data=None, settings=None):
        self.current_screen = screen_name
        self.screen_data = data or {}
        self.game_settings = settings or self.game_settings

        if screen_name == SCREEN_CHOOSE_PLAYER:
            self.choose_player_screen.reset()
        elif screen_name == SCREEN_GAME:
            self.game_screen.game_settings = settings
            self.game_screen.reset()
        elif screen_name == SCREEN_HIGH_SCORES:
            self.high_scores_screen.reset()
        elif screen_name == SCREEN_GAME_OVER:
            score = self.screen_data.get("score", 0)
            self.game_over_screen.set_score(score)

    # Dynamic method to handle events of each screen
    def handle_event(self, event):
        if self.current_screen == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.new_game_button.collidepoint(mouse_pos):
                    self.switch_screen(SCREEN_CHOOSE_PLAYER)
                elif self.high_scores_button.collidepoint(mouse_pos):
                    self.switch_screen(SCREEN_HIGH_SCORES)
                elif self.quit_button.collidepoint(mouse_pos):
                    self._quit_game()
        elif self.current_screen == SCREEN_CHOOSE_PLAYER:
            self.choose_player_screen.handle_event(event)
        elif self.current_screen == SCREEN_GAME:
            self.game_screen.handle_event(event)
        elif self.current_screen == SCREEN_GAME_OVER:
            self.game_over_screen.handle_event(event)
        elif self.current_screen == SCREEN_HIGH_SCORES:
            self.high_scores_screen.handle_event(event)

    # Updates dynamically each screen objects
    def update(self):
        if self.current_screen == SCREEN_CHOOSE_PLAYER:
            self.choose_player_screen.update()
        elif self.current_screen == SCREEN_GAME:
            self.game_screen.update()
            if self.game_screen.game.is_game_over:
                score = self.game_screen.game.get_score()
                self.switch_screen(SCREEN_GAME_OVER, {"score": score})
        elif self.current_screen == SCREEN_GAME_OVER:
            self.game_over_screen.update()
        elif self.current_screen == SCREEN_HIGH_SCORES:
            self.high_scores_screen.update()

    # Handles the dynamic drawing of each screen according to current screen
    def draw(self):
        if self.current_screen == "menu":
            self._draw_menu()
        elif self.current_screen == SCREEN_CHOOSE_PLAYER:
            self.choose_player_screen.draw()
        elif self.current_screen == SCREEN_GAME:
            self.game_screen.draw()
        elif self.current_screen == SCREEN_GAME_OVER:
            self.game_over_screen.draw()
        elif self.current_screen == SCREEN_HIGH_SCORES:
            self.high_scores_screen.draw()

    # Draw the text and buttons on screen
    def _draw_menu(self):
        self.screen.fill(GRAY)

        # Draw the text on screen
        title = FONT_TITLE.render("Space Clash", True, INDIGO)
        subtitle = FONT_DEFAULT.render("An out of space adventure!", True, DARK_GRAY)
        reserved_text = FONT_DEFAULT.render("® All rights reserved to JasonR95 ®", True, BLACK)
        self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 100)))
        self.screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH // 2, 170)))
        self.screen.blit(reserved_text, reserved_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)))

        # Draw buttons on screen
        mouse_pos = pygame.mouse.get_pos()
        self._draw_button(self.new_game_button, "New Game", mouse_pos)
        self._draw_button(self.high_scores_button, "High Scores", mouse_pos)
        self._draw_button(self.quit_button, "Quit", mouse_pos, DARK_RED, RED)

    # Method that build dynamically buttons
    def _draw_button(self, rect, text, mouse_pos, base_color=INDIGO, hover_color=PURPLE):
        color = hover_color if rect.collidepoint(mouse_pos) else base_color
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        label = FONT_BUTTON.render(text, True, WHITE)
        self.screen.blit(label, label.get_rect(center=rect.center))

    # Handle quit event
    def _quit_game(self):
        self.running = False
        pygame.quit()
        sys.exit()

    # Main running method
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_event(event)

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

        self._quit_game()
