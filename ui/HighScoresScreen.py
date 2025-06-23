

from logic.ScoreManager import ScoreManager
from utils.Settings import *
from assets.assets import *


class HighScoresScreen:
    def __init__(self, screen, switch_screen):
        self.screen = screen
        self.switch_screen = switch_screen
        self.score_manager = ScoreManager()

        self.menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT - 80, 250, 50)

    # Have no any dynamic updates
    def update(self):
        pass

    # Draw the table of high scores according to data on the json file, limits to 15 best scores
    def draw(self):
        # self.screen.fill(GRAY)
        self.screen.blit(SPACE_1, (0, 0))

        title = FONT_SMALL_LARGE.render("High Scores", True, WHITE)
        self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 50)))

        y_offset = 120
        records = self.score_manager.get_records()

        if not records:
            no_data = FONT_SMALL.render("No records yet. Be the first!", True, GRAY)
            self.screen.blit(no_data, no_data.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        else:
            headers = [("Rank", 200), ("Name", 400), ("Score", 750), ("Date", 950)]
            for text, x in headers:
                header = FONT_SMALL.render(text, True, WHITE)
                self.screen.blit(header, (x, y_offset))
            y_offset += 40

            for i, record in enumerate(records[:TOP_SCORES_DISPLAY]):
                color = DARK_YELLOW if i < 3 else WHITE

                rank = FONT_SMALL.render(f"{i + 1}.", True, color)
                name = FONT_SMALL.render(record["name"], True, color)
                score = FONT_SMALL.render(str(record["score"]), True, color)
                date = FONT_SMALL.render(record.get("date", "N/A"), True, color)

                self.screen.blit(rank, (200, y_offset))
                self.screen.blit(name, (400, y_offset))
                self.screen.blit(score, (750, y_offset))
                self.screen.blit(date, (950, y_offset))
                y_offset += 30

        # Menu button configuration
        mouse_pos = pygame.mouse.get_pos()
        color = DARK_GRAY if self.menu_button_rect.collidepoint(mouse_pos) else GRAY
        pygame.draw.rect(self.screen, color, self.menu_button_rect, border_radius=5)

        menu_text = FONT_BUTTON.render("Back to Menu", True, BLACK)
        self.screen.blit(menu_text, menu_text.get_rect(center=self.menu_button_rect.center))

    # Handles the menu button to transfer to menu screen
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.menu_button_rect.collidepoint(pygame.mouse.get_pos()):
                self._back_to_menu()

    # Transfer to menu
    def _back_to_menu(self):
        self.switch_screen(SCREEN_MENU)

    # Reset method for screen compatibility
    def reset(self):
        # Refresh score data when showing high scores
        self.score_manager.load_records()
