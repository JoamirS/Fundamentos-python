import random


def play():
    print('-' * 35)
    print("Bem vindo ao jogo da Forca")
    print('-' * 35)

    file = open('words.txt', 'r')
    words_list = []
    for line in file:
        line = line.strip()
        words_list.append(line)
    file.close()

    length_list_secret_number = random.randrange(0, len(words_list))
    word_secret = words_list[length_list_secret_number].upper()

    print(words_list)
    correct_letters = ['_' for letter in word_secret]
    print(correct_letters)

    hanged = False
    correct_word = False
    counter_attempt = 6

    while not hanged and not correct_word:
        attempt_user = input('Qual letra deseja procurar? ')
        attempt_user = attempt_user.strip().upper()

        if attempt_user in word_secret:
            index_word = 0
            for letter in word_secret:
                if attempt_user == letter:
                    correct_letters[index_word] = letter
                index_word += 1
            counter_attempt -= 1
        else:
            counter_attempt -= 1

        missing_letters = correct_letters.count('_')
        if missing_letters > 0:
            print(f'Ainda faltam acertar {missing_letters} letras para vencer.')

        if counter_attempt > 0:
            print(f'Ainda faltam {counter_attempt} rodadas.')
        else:
            hanged = True

        print(correct_letters)
        correct_word = '_' not in correct_letters

    if correct_word:
        print('Você ganhou')
    else:
        print('Você perdeu')
    print("Fim do jogo")


if __name__ == '__main__':
    play()
