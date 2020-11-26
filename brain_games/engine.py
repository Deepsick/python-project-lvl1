import prompt


def run_game(description, rounds):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(description)
    for round in rounds:
        question, correct_answer = round.values()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(
                '\'{}\' is wrong answer ;(. '
                'Correct answer was \'{}\'.'.format(
                    user_answer,
                    correct_answer
                )
            )
            print('Let\'s try again, {}!'.format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
