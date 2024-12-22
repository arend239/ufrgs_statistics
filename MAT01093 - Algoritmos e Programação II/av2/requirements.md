Avaliação a ser entregue:

Regras:
A avaliação pode ser feita em duplas. Entretanto cada aluno deve enviar a sua cópia do trabalho. Indique a dupla do trabalho.

a) Enviar um arquivo.py com o código python
b) uma cópia da tela com o jogo aberto
c) Indicar no email até qual questão foi implementado. Se tiver algum problema indicar onde parou. O Exercício 1 e 2 são obrigatórios para obter nota completa.

para dago@mat.ufrgs.br até segunda-feira 18/nov, 23:59.

Idealmente o tempo aproximado para realizar deveria ser menor que 4 horas.(correspondente as aulas da semana).

Considere o pequeno exemplo com cartas em python.

Código cartas.py  no github

https://github.com/djusto/algoritmos2/blob/master/codigos/cartas.py


Avaliação 2:

Exercício 1 (Obrigatório):
Faça o código necessário para que seja possível mover cartas entre as pilhas.

a) se a pilha estiver vazia não deve dar erro.
b) coloque um limite no máximo de cartas a serem empilhadas.

Exercício 2 (Obrigatório):
c) aumente o número de pilhas para 10 pilhas

d) Coloque uma restrição no valor numérico da carta ao movimentar, tal que, "Somente é possível movimentar uma carta de valor n em cima de uma carta de valor n+1". Ou seja, colocar um 7 preto encima de uma 8 vermelho.

e) Coloque uma restrição para que movimente UMA carta somente se: "as cartas são empilhadas de tal forma a ficarem alternadas nas cores. Ou seja, uma carta vermelha encima de uma carta preta, ou uma preta em cima de uma carta vermelha"

Exercício 3 (extra):

f) Implemente uma regra para que seja possível mover uma subpilha de tamanho no máximo 5 quando as cartas na subpilha estiverem alternadas em cores e na ordem correta numérica (carta n encima de carta n+1)

Exercício 4 (extra2):
g) Implemente as pilhas para recolher as cartas (como no Freecell) na ordem crescente. Ou seja, coloque primeiros os "A", encima dele coloque os 2, depois os 3, de tal forma a ir esvaziando as pilhas. Essas pilhas de recolhimento podem estar no canto superior direito, ou pilhas extras vazias a direita das pilhas atuais (talvez diminuir o tamanho das cartas)