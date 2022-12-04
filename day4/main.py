"""Advent of Code, Day 4

:author: Jeremy Biggs
:date: 12-4-2022
"""
from argparse import ArgumentParser
from typing import List, Tuple


def count_overlapping_cleanup_assignments(
    assignments: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    fully_contained: bool = True,
) -> int:
    """Count overlapping cleanup assignments
    """
    ovelapping = 0
    for elf1, elf2 in assignments:

        elf1_assign = range(elf1[0], elf1[1] + 1)
        elf2_assign = range(elf2[0], elf2[1] + 1)

        if fully_contained and (
                set(elf1_assign).issubset(elf2_assign) or
                set(elf2_assign).issubset(elf1_assign)
            ): 
                ovelapping += 1
        elif not fully_contained and (
                set(elf1_assign).intersection(elf2_assign)
            ):
                ovelapping += 1
    return ovelapping


if __name__ == "__main__":

    parser = ArgumentParser("Advent of Code, Day 4")
    parser.add_argument(
        "-i",
        "--input_file",
        default="./input.txt",
        help="The path to the input file",
    )

    args = parser.parse_args()

    # read in the file
    with open(args.input_file) as buffer:
        assign = [
            tuple([
                tuple([int(i) for i in line.strip().split(",")[0].split("-")]),
                tuple([int(i) for i in line.strip().split(",")[1].split("-")]),
            ])
            for line in buffer.readlines()
        ]

    # Day 4, part 1
    print(count_overlapping_cleanup_assignments(assign))

    # Day 4, part 2
    print(count_overlapping_cleanup_assignments(
        assign, 
        fully_contained=False
    ))
