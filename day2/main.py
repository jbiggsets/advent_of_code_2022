"""Advent of Code, Day 2

:author: Jeremy Biggs
:date: 12-4-2022
"""
from argparse import ArgumentParser
from typing import List, Tuple


CHALLENGE_MAP = {
    "rock": "paper",
    "paper": "scissor",
    "scissor": "rock"
}

CHALLENGE_MAP_REV = {
    v: k for k, v in CHALLENGE_MAP.items()
}

OUTCOME_POINT_MAP = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}

SHAPE_POINT_MAP = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
}

STRATEGY_MAP_ASSUMED = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
    "X": "rock",
    "Y": "paper",
    "Z": "scissor",
}

STRATEGY_MAP_ACTUAL = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


def parse_puzzle_input(filename: str):
    """Parse the puzzle input
    """
    with open(filename) as buffer:
        return [
            tuple(line.strip().split(" "))
            for line in buffer.readlines()
        ]


def play_rock_paper_scissor(
    opponent_shape: str, 
    my_shape: str,
) -> str:
    """Play rock-paper-scissor
    """
    if opponent_shape == my_shape:
        return "draw"
    elif my_shape == CHALLENGE_MAP[opponent_shape]:
        return "win"
    return "lose"

def play_rock_paper_scissor_in_reverse(
    opponent_shape: str, 
    my_strategy: str,
) -> str:
    """Respond to an opponent shape, given a strategy
    """
    if my_strategy == "lose":
        return CHALLENGE_MAP_REV[opponent_shape]
    elif my_strategy == "win":
        return CHALLENGE_MAP[opponent_shape]
    return opponent_shape

def find_score_from_strategy_guide(
    strategies: List[Tuple[str, str]],
    in_reverse: bool = False,
) -> int:
    """Find the score from the given strategy guide
    """
    results = []
    for (opponent, me) in strategies:
        if in_reverse:
            opponent_shape, outcome = (
                STRATEGY_MAP_ACTUAL[opponent],
                STRATEGY_MAP_ACTUAL[me]
            )
            my_shape = play_rock_paper_scissor_in_reverse(
                opponent_shape, outcome
            )
        else:
            opponent_shape, my_shape = (
                STRATEGY_MAP_ASSUMED[opponent],
                STRATEGY_MAP_ASSUMED[me]
            )
            outcome = play_rock_paper_scissor(
                opponent_shape, my_shape
            )
        score = OUTCOME_POINT_MAP[outcome] + SHAPE_POINT_MAP[my_shape]
        results.append(score)
    return sum(results)


if __name__ == "__main__":

    parser = ArgumentParser("Advent of Code, Day 2")
    parser.add_argument(
        "-i",
        "--input_file",
        default="./input.txt",
        help="The path to the input file",
    )

    args = parser.parse_args()

    # read in and parse the file
    strategies = parse_puzzle_input(args.input_file)

    # Day 2, part 1
    print(find_score_from_strategy_guide(strategies))

    # Day 2, part 2
    print(find_score_from_strategy_guide(strategies, in_reverse=True))
