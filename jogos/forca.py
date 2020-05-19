def play():
    print('-' * 35)
    print("Bem vindo ao jogo da Forca")
    print('-' * 35)

    word_secret = "Minions"
    correct_letters = ['_', '_', '_', '_', '_', '_', '_']

    hanged = False
    correct_word = False

    print(correct_letters)

    while not hanged and not correct_word:
        attempt_user = input('Qual letra deseja procurar? ')
        attempt_user = attempt_user.strip()

        index_word = 0
        for letter in word_secret:
            if attempt_user.upper() == letter.upper():
                correct_letters[index_word] = letter
            index_word += 1

        missing_letters = correct_letters.count('_')
        if missing_letters > 0:
            print(f'Ainda faltam acertar {missing_letters} letras para vencer.')
        else:
            print('Você acertou todas as letras.')
            break

        print(correct_letters)

    print("Fim do jogo")


if __name__ == '__main__':
    play()
