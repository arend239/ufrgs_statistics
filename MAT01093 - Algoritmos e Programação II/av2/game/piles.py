from game.cards import card

def create_deck():

    import random
    deck = [card(i, j) for i in range(1, 14) for j in range(4)]
    random.shuffle(deck)
    return deck

def mount_piles(deck, n_piles):

    piles = [[] for _ in range(n_piles)]
    for i, card in enumerate(deck):
        piles[i % n_piles].append(card)
    return piles

def draw_pile(pile, i_col, screen_width, n_col, y_ini = 50):

    sec_width  = screen_width // n_col
    sec_center = i_col * sec_width + sec_width // 2
    for i, card in enumerate(pile):
        card.draw(sec_center - 50, y_ini + i * 30)