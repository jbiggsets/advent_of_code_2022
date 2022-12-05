"""Advent of Code, Day 5

:author: Jeremy Biggs
:date: 12-5-2022
"""
import re
from argparse import ArgumentParser
from copy import deepcopy
from typing import List, Tuple


REGEX = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")


def parse_puzzle_input(filename: str):
    """Parse the puzzle input
    """
    with open(filename) as buffer:
        raw = buffer.read()

    # get the crate rows and the moves
    crates = raw[:raw.find("\n\n")].split("\n")
    moves = raw[raw.find("\n\n"):].strip()

    # get the indexes of the crates
    idxes = [int(idx) 
        for idx, char in enumerate(crates[-1]) 
        if char.strip()
    ]

    # get the crates
    crates = [
        [crt for idx, crt in enumerate(row) if idx in idxes]
        for row in crates[:-1]
    ]

    # get the moves
    moves = REGEX.findall(moves)
    moves = [(int(a), int(b) - 1, int(c) - 1) for a, b, c in moves]
    return crates, moves


def relocate_the_crates(
    crates: List[List[str]],
    moves: List[Tuple[int, int, int]],
    multiple: bool = False
):
    """Relocate the crates, given instructions
    """
    # create a transposed list of crates
    tcrates = list(zip(*deepcopy(crates)))
    tcrates = [[c for c in row if c.strip()] for row in tcrates]
    for number, start_crate, end_crate in moves:

        # move multiple crates at the same time
        if multiple:
            group = tcrates[start_crate][:number]
            tcrates[end_crate] = group + tcrates[end_crate]
            del tcrates[start_crate][:number]

        # move one crate at a time
        else:
            for _ in range(number):
                crate = tcrates[start_crate].pop(0)
                tcrates[end_crate].insert(0, crate)

    return "".join([row[0] for row in tcrates])



if __name__ == "__main__":

    parser = ArgumentParser("Advent of Code, Day 5")
    parser.add_argument(
        "-i",
        "--input_file",
        default="./input.txt",
        help="The path to the input file",
    )

    args = parser.parse_args()

    # read in and parse the file
    crates, moves = parse_puzzle_input(args.input_file)

    # Day 5, part 1
    print(relocate_the_crates(crates, moves))

    # Day 5, part 2
    print(relocate_the_crates(crates, moves, multiple=True))
