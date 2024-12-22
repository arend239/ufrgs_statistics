import random
import pygame
import sys

pygame.init()
info = pygame.display.Info()
largura, altura = info.current_w, info.current_h
tela = pygame.display.set_mode((1040, 624))

# largura, altura = 800, 800
# tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Carta de Baralho')

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
class Carta:
    def __init__(self,valor,naipe):
        self.valor=valor
        self.naipe=naipe


    def desenha(self,x,y):
        desenhar_carta(tela,100+ x*100,y*50, self.valor,self.naipe)

    def __str__(self):
        return (self.valor,self.naipe)

def desenhar_carta(superficie, pos_x, pos_y, valor, naipe):
    largura_carta = 95
    altura_carta = 150
    pygame.draw.rect(superficie, branco, (pos_x, pos_y, largura_carta, altura_carta), border_radius=10)
    pygame.draw.rect(superficie, preto, (pos_x, pos_y, largura_carta, altura_carta), 3, border_radius=10)

    # Definindo fonte e renderizando o valor da carta
    fonte_valor = pygame.font.SysFont(None, 40)

    valores= {1: 'A', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
    naipes = {0: '♠', 1: '♣', 2: '♥', 3: '♦'}

    cor = preto if naipe in [0,1] else vermelho

    texto_valor = fonte_valor.render(valores[valor], True, cor)
    tela.blit(texto_valor, (pos_x + 10, pos_y + 10))

    # Desenhar o símbolo do naipe usando o Unicode
    fonte_naipe = pygame.font.SysFont('Courier', 35)
    texto_naipe = fonte_naipe.render(naipes[naipe], True, cor)
    tela.blit(texto_naipe, (pos_x + 10, pos_y + 25))



def printpilha(P,x,y):
    for k in range(len(P)):
        P[k].desenha(x,y+k)



# Dimensões da matriz
ncartas = 5
npilhas = 3

# Criar uma matriz 5x4 com zeros
P = [[Carta(0,0) for _ in range(ncartas)] for _ in range(npilhas)]

for p in range(npilhas):
    for c in range(ncartas):
        v=random.randint(1,13)
        n=random.randint(0,3)
        print(p,c)
        P[p][c]= Carta(v,n)


# Loop principal do jogo
rodando = True
escolha = 0
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            cx=x//100
            cy=y//50
            print(f'Clique em: {x,y} ==> {cx,cy}')
            if escolha==0:
                # escolheu origem
                escolha=cx
                origem =escolha-2
            else:
                # escolheu destino
                escolha=0
                destino=cx-2
                print(f'Retirar {origem} mover para {destino}')

                c=P[origem].pop()
                P[destino].append(c)




    # Preencher o fundo da tela
    tela.fill((0, 128, 0))  # Fundo verde como uma mesa de jogo

    printpilha(P[0],1,1)
    printpilha(P[1],2,1)
    printpilha(P[2],3,1)

    #desenhar_carta(tela, largura//2 - 50, altura//2 - 75, 'A', '♠')

    # Atualizar a tela
    pygame.display.flip()

# Encerrando o Pygame
pygame.quit()
sys.exit()



