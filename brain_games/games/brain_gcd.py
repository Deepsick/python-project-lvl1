from math import gcd
from brain_games.engine import run_game
from brain_games.const import ROUNDS_COUNT
from brain_games.utils import generate_random_number


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_number = generate_random_number(0, 12)
    second_number = generate_random_number(0, 15)
    question = '{} {}'.format(first_number, second_number)
    correct_answer = gcd(first_number, second_number)
    return {
        'question': question,
        'correct_answer': str(correct_answer)
    }


def start():
    rounds = []
    for _ in range(ROUNDS_COUNT):
        round = generate_round()
        rounds.append(round)
    run_game(DESCRIPTION, rounds)
