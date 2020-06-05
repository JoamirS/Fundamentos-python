import random
from time import sleep

list_all_attempts = list()


def play():
    print_opening_message()

    word_secret = load_secret_word()

    correct_letters = initializes_correct_letters(word_secret)

    print(correct_letters)

    hanged = False
    correct_word = False
    mistake = 0
    total_attempt = 1

    while not hanged and not correct_word:
        print(f'Esta é {total_attempt}ª rodada.')
        print(list_all_attempts)
        attempt_user = get_attempt()

        if attempt_user in word_secret:
            mark_kick_right(secret_word_input=word_secret, attempt_user_input=attempt_user, correct_letters_input=correct_letters)
        else:
            mistake += 1
            draw_hanged(mistake)

        list_all_attempts.append(attempt_user)

        print(f'Você possui {mistake} erros.')
        total_attempt += 1

        hanged = mistake == 7
        correct_word = '_' not in correct_letters

        print(correct_letters)

    if correct_word:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(word_secret))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print("Fim do jogo")


def print_opening_message():
    print('-' * 35)
    print("Bem vindo ao jogo da Forca")
    print('-' * 35)


def load_secret_word():
    file = open('words.txt', 'r')
    words_list = []

    for line in file:
        line = line.strip()
        words_list.append(line)

    file.close()

    length_list_secret_number = random.randrange(0, len(words_list))
    word_secret = words_list[length_list_secret_number].upper()
    return word_secret


def initializes_correct_letters(word_secret):
    return ['_' for letter in word_secret]


def get_attempt():
    attempt = input('Qual a letra? ')
    attempt = attempt.strip().upper()
    attempt_in_validation = attempt_already_made(attempt)

    if attempt_in_validation:
        print('Você já digitou essa letra, tente novamente.')
        get_attempt()
    else:
        print('Validando .', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
    return attempt


def attempt_already_made(attempt_to_be_validated):
    for letter in list_all_attempts:
        if attempt_to_be_validated == letter:
            return True
        else:
            return False


def mark_kick_right(secret_word_input, attempt_user_input, correct_letters_input):
    index_word = 0

    for letter in secret_word_input:
        if attempt_user_input == letter:
            correct_letters_input[index_word] = letter
        index_word += 1


def draw_hanged(mistake_input):
    print("  _______     ")
    print(" |/      |    ")

    if mistake_input == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if mistake_input == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if mistake_input == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if mistake_input == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if mistake_input == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if mistake_input == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if mistake_input == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    play()
