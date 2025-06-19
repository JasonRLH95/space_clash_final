
from p2.logic.ScoreManager import ScoreManager
from p2.utils.Settings import *


class GameOverScreen:
    def __init__(self, screen, switch_screen):
        self.screen = screen
        self.switch_screen = switch_screen
        self.score_manager = ScoreManager()

        self.name_input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50)
        self.save_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 120, 300, 60)
        self.menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 200, 300, 60)

        self.player_name = ""
        self.name_input_active = False
        self.current_score = 0

    # Catch the score from the game after game over
    def set_score(self, score):
        self.current_score = score
        self.score_manager.current_score = score

    # Handle the events of type the input or pressing the buttons
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.name_input_rect.collidepoint(mouse_pos):
                self.name_input_active = True
            else:
                self.name_input_active = False

            if self.save_button_rect.collidepoint(mouse_pos):
                self._save_score()
            elif self.menu_button_rect.collidepoint(mouse_pos):
                self._back_to_menu()

        if event.type == pygame.KEYDOWN and self.name_input_active:
            if event.key == pygame.K_RETURN:
                self._save_score()
            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            else:
                if len(self.player_name) < MAX_NAME_LENGTH:
                    self.player_name += event.unicode

    # No any dynamic updates needed
    def update(self):
        pass

    # Draw the headers, input and buttons
    def draw(self):
        self.screen.fill(GRAY)

        title = FONT_TITLE.render("Game Over!", True, RED)
        score = FONT_BUTTON.render(f"Your Score: {self.current_score}", True, BLACK)
        label = FONT_DEFAULT.render("Enter Your Name:", True, BLACK)
        name_text = FONT_DEFAULT.render(self.player_name, True, BLACK)

        # Define and draw the headers
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        score_rect = score.get_rect(center=(SCREEN_WIDTH // 2, 200))
        label_rect = label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

        self.screen.blit(title, title_rect)
        self.screen.blit(score, score_rect)
        self.screen.blit(label, label_rect)

        # Draw the text input
        box_color = WHITE if self.name_input_active else DARK_GRAY
        pygame.draw.rect(self.screen, box_color, self.name_input_rect, border_radius=5)
        pygame.draw.rect(self.screen, DARK_GRAY, self.name_input_rect, 2, border_radius=5)
        self.screen.blit(name_text, (self.name_input_rect.x + 10, self.name_input_rect.y + 10))

        mouse_pos = pygame.mouse.get_pos()

        # Draw save scores button
        save_color = GREEN if self.save_button_rect.collidepoint(mouse_pos) else DARK_GREEN
        pygame.draw.rect(self.screen, save_color, self.save_button_rect, border_radius=5)
        save_text = FONT_BUTTON.render("Save Scores", True, WHITE)
        self.screen.blit(save_text, save_text.get_rect(center=self.save_button_rect.center))

        # Draw menu button
        menu_color = PURPLE if self.menu_button_rect.collidepoint(mouse_pos) else INDIGO
        pygame.draw.rect(self.screen, menu_color, self.menu_button_rect, border_radius=5)
        menu_text = FONT_BUTTON.render("Menu", True, WHITE)
        self.screen.blit(menu_text, menu_text.get_rect(center=self.menu_button_rect.center))

    # Insert the scores to the highscores file and transfer to HighScoresScreen
    def _save_score(self):
        if self.score_manager.save_record(self.player_name):
            self.player_name = ""
            self.switch_screen(SCREEN_HIGH_SCORES)

    # Transfer back to menu screen
    def _back_to_menu(self):
        self.player_name = ""
        self.switch_screen(SCREEN_MENU)
