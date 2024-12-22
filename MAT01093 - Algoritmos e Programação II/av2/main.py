import pygame
import sys

from game.config import screen, screen_width, screen_height, suits, colors, draw_div
from game.piles  import draw_pile, create_deck, mount_piles

def def_num_piles():

    font       = pygame.font.SysFont('Courier', 32)
    is_running = True
    n          = 8

    while is_running:
        screen.fill(colors.green)
        screen_question = font.render("Number of stacks (5 to 10):", True, colors.white)
        screen_number   = font.render(str(n), True, colors.l_green)
        screen_b_suits  = font.render("♠ ♣",  True, colors.black)
        screen_r_suits  = font.render("♥ ♦", True, colors.red)

        screen.blit(screen_question, (150, 200))
        screen.blit(screen_number, (750, 200))

        screen.blit(screen_b_suits, (150, 250))
        screen.blit(screen_r_suits, (230, 250))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_UP   and n < 10:
                    n += 1
                elif event.key == pygame.K_DOWN and n > 5:
                    n -= 1
                elif event.key == pygame.K_RETURN:
                    return n

def main():

    n_piles = def_num_piles()
    sec_width = (screen_width // n_piles)

    deck   = create_deck()
    piles = mount_piles(deck, n_piles)

    pile_card_limit = 18

    select        = 0
    home = target = -1
    n_cards_move  = 1
    home_sec      = None

    is_running = True
    while is_running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos
                home_sec = cx = x // (screen_width // n_piles)
                print(f'click: {x, y} => col {cx}')

                if select == 0:
                    home   = cx
                    select = 1

                else:
                    target = cx

                    if target == home:
                        if n_cards_move != 5 and len(piles[home]) >  n_cards_move:

                            mv1_card_number = piles[home][- (n_cards_move)].value
                            mv1_card_suit   = piles[home][- (n_cards_move)].suit

                            mv2_card_number = piles[home][- (n_cards_move + 1)].value
                            mv2_card_suit   = piles[home][- (n_cards_move + 1)].suit

                            print(f'acumm: \n'
                                  f'{mv1_card_number} ; {suits[mv1_card_suit]} \n'
                                  f'{mv2_card_number} ; {suits[mv2_card_suit]}')

                            if (mv1_card_suit in [0, 1]) != (mv2_card_suit in [0, 1]) and (mv1_card_number + 1) == mv2_card_number:
                                n_cards_move += 1

                    if  home != target and  len(piles[target]) < pile_card_limit:

                        home_number, home_suit = piles[home][-n_cards_move].value, piles[home][-n_cards_move].suit
                        targ_number, targ_suit = piles[target][-1].value, piles[target][-1].suit

                        print(f"home: {home_number} ; {suits[home_suit]}")
                        print(f"targ: {targ_number} ; {suits[targ_suit]}")

                        if (home_suit in [0, 1]) != (targ_suit in [0, 1]) and (home_number + 1 == targ_number):

                            pile_transfer = piles[home][-n_cards_move:]
                            piles[home]   = piles[home][:-n_cards_move]
                            piles[target].extend(pile_transfer)

                        n_cards_move = 1

                    if target != home:
                        select = 0

        screen.fill(colors.green)

        for i, pile in enumerate(piles):
            if i == home_sec and select == 1:
                pygame.draw.rect(screen, colors.d_green, (i * sec_width, 0, sec_width, screen_height))
            draw_pile(pile, i, screen_width, n_piles)

        draw_div(screen, screen_width, screen_height, n_piles)

        if n_cards_move > 1:
            count_n_cards_move = pygame.font.SysFont(None, 18).render(str(n_cards_move), True, colors.l_green)
            x_sec_center = home_sec * sec_width + sec_width // 2
            screen.blit(count_n_cards_move, (x_sec_center, screen_height - 24))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()