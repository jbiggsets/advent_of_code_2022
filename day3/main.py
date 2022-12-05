"""Advent of Code, Day 3

:author: Jeremy Biggs
:date: 12-4-2022
"""
from argparse import ArgumentParser
from functools import reduce
from string import ascii_letters
from typing import List


def parse_puzzle_input(filename: str):
    """Parse the puzzle input
    """
    with open(filename) as buffer:
        return [
            line.strip()
            for line in buffer.readlines()
        ]


def find_rucksack_priorities(
    sacks: List[str],
) -> int:
    """Find the rucksack priority sum
    """
    priorities = []
    for sack in sacks:
        lower, upper = (
            sack[:len(sack) // 2],
            sack[len(sack) // 2:]
        )
        intersect = set(lower).intersection(upper)
        priorities.extend([
            ascii_letters.index(i) + 1 for i in intersect
        ])
    return sum(priorities)


def find_badge_priorities(
    sacks: List[str],
    size: int = 3,
) -> int:
    """Find the badge priority sum
    """
    priorities = []
    for group_i in range(size, len(sacks) + 1, size):

        # get the group of `size`
        group = sacks[group_i - size: group_i]
        group = [set(sack) for sack in group]

        # get the intersection across members of the group
        intersect = (
            reduce(lambda x, y: x & y, group)
        ) 
        priorities.extend([
            ascii_letters.index(i) + 1 for i in intersect
        ])
    return sum(priorities)


if __name__ == "__main__":

    parser = ArgumentParser("Advent of Code, Day 3")
    parser.add_argument(
        "-i",
        "--input_file",
        default="./input.txt",
        help="The path to the input file",
    )

    args = parser.parse_args()

    # read in and parse the file
    sacks = parse_puzzle_input(args.input_file)

    # Day 3, part 1
    print(find_rucksack_priorities(sacks))

    # Day 3, part 2
    print(find_badge_priorities(sacks))

