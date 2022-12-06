"""Advent of Code, Day 6

:author: Jeremy Biggs
:date: 12-6-2022
"""
from argparse import ArgumentParser


def parse_puzzle_input(filename: str):
    """Parse the puzzle input
    """
    with open(filename) as buffer:
        return [line.strip() for line in buffer.readlines()]


def get_start_of_packet_with_seq_of_n(
    characters: str, 
    n: int = 4
):
    """Get the start of packet with a sequence length of N
    """
    for i in range(len(characters) - n):
        seq = characters[i: i + n]
        if len(set(seq)) == n:
            return i + n


if __name__ == "__main__":

    parser = ArgumentParser("Advent of Code, Day 6")
    parser.add_argument(
        "-i",
        "--input_file",
        default="./input.txt",
        help="The path to the input file",
    )

    args = parser.parse_args()

    # read in and parse the file
    character_lines = parse_puzzle_input(args.input_file)

    # Day 6, part 1
    for characters in character_lines:
        print(get_start_of_packet_with_seq_of_n(characters))

    # Day 6, part 1
    for characters in character_lines:
        print(get_start_of_packet_with_seq_of_n(characters, n=14))
