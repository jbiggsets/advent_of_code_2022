"""Advent of Code, Day 1

:author: Jeremy Biggs
:date: 12-4-2022
"""
from argparse import ArgumentParser
from typing import List 


def find_sum_of_elves_with_top_n_calories(
    food: List[str], 
    n: int = 1
) -> int:
    """Find sum of calories for the to N elves.
    """
    # loop through the items and get the set of items for each elf
    elf_i, elves = 0, [[]]
    for item in food:
        if item.strip() == "":
            elves.append([])
            elf_i += 1; continue
        elves[elf_i].append(int(item.strip()))

    # get the calories for each elf
    calories = sorted([sum(elf) for elf  in elves], reverse=True)
    return sum(calories[:n])


if __name__ == "__main__":

    parser = ArgumentParser("Advent of Code, Day 1")
    parser.add_argument(
        "-i",
        "--input_file",
        default="./input.txt",
        help="The path to the input file",
    )

    args = parser.parse_args()

    # read in the file
    with open(args.input_file) as buffer:
        elements = buffer.readlines()

    # Day 1, part 1
    print(find_sum_of_elves_with_top_n_calories(elements))

    # Day 1, part 2
    print(find_sum_of_elves_with_top_n_calories(elements, n=3))
