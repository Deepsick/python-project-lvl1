from brain_games.engine import run_game
from brain_games.const import ROUNDS_COUNT
from brain_games.utils import generate_random_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if(number % i == 0):
            return False
    return True


def generate_round():
    number = generate_random_number(0, 50)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return {
        'question': str(number),
        'correct_answer': correct_answer
    }


def start():
    rounds = []
    for _ in range(ROUNDS_COUNT):
        round = generate_round()
        rounds.append(round)
    run_game(DESCRIPTION, rounds)
