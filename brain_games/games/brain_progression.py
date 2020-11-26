from brain_games.engine import run_game
from brain_games.const import ROUNDS_COUNT
from brain_games.utils import generate_random_number

DESCRIPTION = 'What number is missing in the progression?'
HIDDEN_MARK = '..'


def generate_progression(start, step, length):
    return [start + step * index for index in range(length)]


def get_question(numbers, index):
    sliced_numbers = numbers[:]
    sliced_numbers[index] = HIDDEN_MARK
    return ' '.join([str(number) for number in sliced_numbers])


def generate_round():
    progression_step = generate_random_number(0, 20)
    progression_start = generate_random_number(0, 100)
    progression_length = generate_random_number(5, 10)
    numbers = generate_progression(
        progression_start,
        progression_step,
        progression_length
    )
    hidden_index = generate_random_number(0, len(numbers) - 1)
    return {
        'question': get_question(numbers, hidden_index),
        'correct_answer': str(numbers[hidden_index])
    }


def start():
    rounds = []
    for _ in range(ROUNDS_COUNT):
        round = generate_round()
        rounds.append(round)
    run_game(DESCRIPTION, rounds)
