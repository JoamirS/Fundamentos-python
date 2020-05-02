import advinhacao
import forca


def choice_game():
    print('-' * 35)
    print("Escolha o seu jogo")
    print('-' * 35)

    print('Opção 1: Forca | Opção 2: Advinhação ')
    option_game_user = int(input('Qual jogo você deseja? '))

    if option_game_user == 1:
        print('Jogo da forca escolhido')
        forca.play()
    elif option_game_user == 2:
        print('Jogo da Advinhação escolhido')
        advinhacao.play()


if __name__ == '__main__':
    choice_game()