import random as rn

class Jokepnpo:
    def __init__(self, nome, jogada):
        self.gerador = rn.choice(['Pedra','Papel','Tesoura'])
        self.jogada = jogada
        self.nome = nome

    def regras(self, jogada, nome):
        nome = self.nome
        jogada = self.jogada
        if self.gerador == 'Pedra':
            if jogada == 'Papel':
                print(f'A máquina jogou {self.gerador}')
                print(f'{nome} ganhou!!')
            else:
                print(f'A máquina jogou {self.gerador}')
                print(f'{nome} perdeu!!')

        if self.gerador == 'Tesoura':
            if jogada == 'Pedra':
                print(f'A máquina jogou {self.gerador}')
                print(f'{nome} ganhou!!')
            else:
                print(f'A máquina jogou {self.gerador}')
                print(f'{nome} perdeu!!')

        if self.gerador == 'Papel':
            if jogada == 'Tesoura':
                print(f'A máquina jogou {self.gerador}')
                print(f'{nome} ganhou!!')
            else:
                print(f'A máquina jogou {self.gerador}')
                print(f'{nome} perdeu!!')

        if self.gerador == jogador:
            print(f'A máquina jogou {self.gerador}')
            print(f'Empate!!')

print('Jokenpo')
jogador = input('Digite o nome do jogador:')
jogada = input('Faça a sua jogada:')
teste = Jokepnpo(jogador,jogada)

teste.regras(jogada,jogador)
