from random import choice
from brain_games.engine import run_game
from brain_games.const import ROUNDS_COUNT
from brain_games.utils import generate_random_number


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']

map_operator_to_operation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y
}


def calculate(a, b, operator):
    return map_operator_to_operation[operator](a, b)


def generate_round():
    first_number = generate_random_number(10, 15)
    second_number = generate_random_number(10, 10)
    operator = choice(OPERATORS)
    question = '{} {} {}'.format(first_number, operator, second_number)
    correct_answer = calculate(first_number, second_number, operator)
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
