import random


def play():
    print('-' * 35)
    print("Bem vindo ao jogo de Adivinhação!")
    print('-' * 35)

    secret_number = random.randrange(1, 101)
    total_attempts = 3
    options_difficulty_level = (1, 2, 3)
    total_points = 1000

    print('Qual nível de dificuldade você deseja? \n Fácil: 1 | Médio: 2 | Difícil: 3')

    difficulty_level_input_user = int(input('Digite uma das 3 opções: '))
    while difficulty_level_input_user not in options_difficulty_level:
        print('Digite uma opção válida.')
        difficulty_level_input_user = int(input('Difite uma das 3 opções: '))

    if difficulty_level_input_user == 1:
        print('Você escolheu o nível fácil, neste caso, você terá 20 tentivas.')
        total_attempts = 20

    if difficulty_level_input_user == 2:
        print('Você escolheu o nível médio, neste caso, você terá 10 tentivas.')
        total_attempts = 10

    if difficulty_level_input_user == 3:
        print('Você escolheu o nível difícil, neste caso, você terá 5 tentivas.')
        total_attempts = 5

    for attempt in range(1, total_attempts + 1):
        print("Tentativa {} de {}".format(attempt, total_attempts))

        user_attempt = int(input("Digite um número entre 1 e 100: "))

        if user_attempt < 1 or user_attempt > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        correct_attempt = user_attempt == secret_number
        number_greater_than_the_secret_number = user_attempt > secret_number
        number_less_than_the_secret_number = user_attempt < secret_number

        if correct_attempt:
            print("Você acertou!")
            break
        else:
            if number_greater_than_the_secret_number:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            if number_less_than_the_secret_number:
                print("Você errou! O seu chute foi menor do que o número secreto.")

            points_lost_with_each_mistake = abs(secret_number - user_attempt)
            total_points -= points_lost_with_each_mistake

    print(f'Sua pontuação final é {total_points}')
    print("Fim do jogo")