
from p2.assets.assets import *


class ChoosePlayerScreen:
    def __init__(self, screen, switch_screen):
        self.screen = screen
        self.switch_screen = switch_screen  # callback to change screens

        # Default selections: first option in each category is selected.
        self.selected_bg_index = 0
        self.selected_ship_index = 0
        self.selected_bullet_index = 0

        # Define dimensions and margins for options
        self.option_spaceship_size = (100, 80)
        self.option_bg_size = (200, 120)
        self.option_margin = 20

        # Buttons surfaces
        self.backgrounds = [SPACE_1, SPACE_2, SPACE_3, SPACE_4]
        self.ships = [WHITE_SPACESHIP, RED_SPACESHIP, YELLOW_SPACESHIP, BLUE_SPACESHIP]
        self.bullet_colors = [BLUE, RED, GREEN, YELLOW, INDIGO, LIGHT_SKY_BLUE, ORANGE, PURPLE, AQUA]

        # Create option groups.
        self._init_background_options()
        self._init_spaceship_options()
        self._init_bullet_options()

        # Play button configuration
        button_width, button_height = 200, 60
        self.play_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT - button_height - 20,
                                            button_width, button_height)
        # Back button configuration
        self.back_button_rect = pygame.Rect((50, 20, button_width - 60, button_height))

    # Create the group of background options
    def _init_background_options(self):
        self.bg_choices = []
        option_w, option_h = self.option_bg_size

        # Calculate total width and starting x coordinate.
        total_width = len(self.backgrounds) * option_w + (len(self.backgrounds) - 1) * self.option_margin
        start_x = (SCREEN_WIDTH - total_width) // 2
        y = 150

        for bg in self.backgrounds:
            surface = pygame.Surface(self.option_bg_size)
            surface.blit(pygame.transform.scale(bg, self.option_bg_size), (0, 0))
            rect = surface.get_rect(topleft=(start_x, y))
            self.bg_choices.append((surface, rect))
            start_x += option_w + self.option_margin

    # Create the group of ships options
    def _init_spaceship_options(self):
        self.spaceship_choices = []
        option_w, option_h = self.option_spaceship_size

        total_width = len(self.ships) * option_w + (len(self.ships) - 1) * self.option_margin
        start_x = (SCREEN_WIDTH - total_width) // 2
        y = 370

        for ship in self.ships:
            surface = pygame.Surface(self.option_spaceship_size)
            surface.blit(pygame.transform.scale(ship, self.option_spaceship_size), (0, 0))
            rect = surface.get_rect(topleft=(start_x, y))
            self.spaceship_choices.append((surface, rect))
            start_x += option_w + self.option_margin

    # Create the group of bullet options
    def _init_bullet_options(self):
        self.bullet_choices = []

        radius = 30
        diameter = radius * 2
        total_width = len(self.bullet_colors) * diameter + (len(self.bullet_colors) - 1) * self.option_margin
        start_x = (SCREEN_WIDTH - total_width) // 2
        y = 550

        for color in self.bullet_colors:
            rect = pygame.Rect(start_x, y, diameter, diameter)
            self.bullet_choices.append((color, rect))
            start_x += diameter + self.option_margin

    # Handle the buttons selections for each section
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            # Check if one of the background options is clicked.
            for i, (_, rect) in enumerate(self.bg_choices):
                if rect.collidepoint(pos):
                    self.selected_bg_index = i
            # Check if one of the spaceship options is clicked.
            for i, (_, rect) in enumerate(self.spaceship_choices):
                if rect.collidepoint(pos):
                    self.selected_ship_index = i
            # Check if one of the bullet color circles is clicked.
            for i, (_, rect) in enumerate(self.bullet_choices):
                if rect.collidepoint(pos):
                    self.selected_bullet_index = i
            # Check if the play button is clicked.
            if self.play_button_rect.collidepoint(pos):
                self._start_game()
            # Check if the back button is clicked.
            if self.back_button_rect.collidepoint(pos):
                self.switch_screen(SCREEN_MENU)

    # set the settings selected and transfer it to the next game screen
    def _start_game(self):
        # Package the chosen settings
        settings = {
            "background": self.backgrounds[self.selected_bg_index],
            "spaceship": self.ships[self.selected_ship_index],
            "bullet_color": self.bullet_colors[self.selected_bullet_index],
        }
        self.switch_screen(SCREEN_GAME, None, settings)

    def update(self):
        # No dynamic elements need periodical updates.
        pass

    # Draw the headers and buttons groups on the screen
    def draw(self):
        self.screen.fill(GRAY)

        # Draw the Back button.
        mouse_pos = pygame.mouse.get_pos()
        button_color = PURPLE if self.back_button_rect.collidepoint(mouse_pos) else INDIGO
        pygame.draw.rect(self.screen, button_color, self.back_button_rect, border_radius=10)
        back_text = FONT_BUTTON.render("Back", True, WHITE)
        self.screen.blit(back_text, back_text.get_rect(center=self.back_button_rect.center))

        # Draw headers for each option group.
        header_bg = FONT_TITLE.render("Choose Background", True, INDIGO)
        header_ship = FONT_TITLE.render("Choose Spaceship", True, INDIGO)
        header_bullet = FONT_TITLE.render("Choose Bullets Color", True, INDIGO)

        self.screen.blit(header_bg, header_bg.get_rect(center=(SCREEN_WIDTH // 2, 100)))
        self.screen.blit(header_ship, header_ship.get_rect(center=(SCREEN_WIDTH // 2, 320)))
        self.screen.blit(header_bullet, header_bullet.get_rect(center=(SCREEN_WIDTH // 2, 500)))

        # Draw background option images.
        for i, (surf, rect) in enumerate(self.bg_choices):
            self.screen.blit(surf, rect)
            # Draw a border if selected.
            if i == self.selected_bg_index:
                pygame.draw.rect(self.screen, WHITE, rect, 4)

        # Draw spaceship option images.
        for i, (surf, rect) in enumerate(self.spaceship_choices):
            self.screen.blit(surf, rect)
            if i == self.selected_ship_index:
                pygame.draw.rect(self.screen, WHITE, rect, 4)

        # Draw bullet options as circles.
        for i, (color, rect) in enumerate(self.bullet_choices):
            center = rect.center
            radius = rect.width // 2
            pygame.draw.circle(self.screen, color, center, radius)
            # If selected, draw a border circle.
            if i == self.selected_bullet_index:
                pygame.draw.circle(self.screen, WHITE, center, radius, 4)
            else:
                pygame.draw.circle(self.screen, BLACK, center, radius, 3)

        # Draw the Play button.
        mouse_pos = pygame.mouse.get_pos()
        button_color = PURPLE if self.play_button_rect.collidepoint(mouse_pos) else INDIGO
        pygame.draw.rect(self.screen, button_color, self.play_button_rect, border_radius=10)
        play_text = FONT_BUTTON.render("Play", True, WHITE)
        self.screen.blit(play_text, play_text.get_rect(center=self.play_button_rect.center))

    # Reset the screen so that the default options are selected.
    def reset(self):
        self.selected_bg_index = 0
        self.selected_ship_index = 0
        self.selected_bullet_index = 0
