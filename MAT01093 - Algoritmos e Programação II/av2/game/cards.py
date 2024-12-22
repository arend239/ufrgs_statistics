import pygame
from game.config import colors, screen_width, screen_height, screen, card_numbers, suits

class card:

    def __init__(self, value, suit):
        self.value  = value
        self.suit   = suit
        self.width  = 95
        self.height = 150

    def draw(self, x, y):
        draw_card(screen, x, y, self.value, self.suit, self.width, self.height)

def draw_card(base, pos_x, pos_y, value, suit, card_x, card_y):

    pygame.draw.rect(base, colors.white, (pos_x, pos_y, card_x, card_y), border_radius=10)
    pygame.draw.rect(base, colors.black, (pos_x, pos_y, card_x, card_y), 3, border_radius=10)

    card_color = colors.black if suit in [0, 1] else colors.red

    font_value = pygame.font.SysFont(None, 35)
    s_text       = font_value.render(card_numbers[value], True, card_color)
    base.blit(s_text, (pos_x + 15, pos_y + 10))

    font_suit = pygame.font.SysFont('Courier', 32)
    s_suit    = font_suit.render(suits[suit], True, card_color)
    base.blit(s_suit, (pos_x + 60, pos_y + 6))
