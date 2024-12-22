import pygame

pygame.init()
info = pygame.display.Info()

# screen_width, screen_height = info.current_w, info.current_h
screen_width, screen_height = 1040, 624
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('avaliacao2_algoritmos')

class colors:
    black   = (000, 000, 000)
    white   = (255, 255, 255)
    gray    = (180, 180, 180)
    red     = (255, 000, 000)
    green   = (000, 128, 000)
    d_green = (000, 100, 000)
    l_green = (100, 255, 000)

suits = {0: '♠', 1: '♣', 2: '♥', 3: '♦'}

card_numbers = {1: 'A',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: '10',
                11: 'J',
                12: 'Q',
                13: 'K'}

def draw_div(base, width, height, n_col):

    line_width = 1
    for i in range(1, n_col):
        x = i * (width // n_col)
        pygame.draw.line(base, colors.gray, (x, 0), (x, height), line_width)