def play():
    print('-' * 35)
    print("Bem vindo ao jogo da Forca")
    print('-' * 35)

    word_secret = "Minions"
    hanged = False
    correct_word = False

    while not hanged and not correct_word:
        attempt_user = input('Qual letra deseja procurar? ')
        attempt_user = attempt_user.strip()

        index_word = 0
        for word in word_secret:
            if attempt_user.upper() == word.upper():
                print(f'Encontrei a letra {word} na posição {index_word}')
            index_word += 1

        print('Jogando')

    print("Fim do jogo")


if __name__ == '__main__':
    play()
