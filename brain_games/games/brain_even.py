
from brain_games.engine import run_game
from brain_games.const import ROUNDS_COUNT
from brain_games.utils import generate_random_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = generate_random_number(0, 20)
    correct_answer = 'yes' if is_even(number) else 'no'
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
