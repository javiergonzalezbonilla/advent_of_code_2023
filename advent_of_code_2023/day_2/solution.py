# -*- coding: utf-8 -*-
import os
import re
from math import prod
from advent_of_code_2023.utils import ReadFile

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def solution1(data):
    result = 0
    for line in data:
        (game_id, cube_sets) = _parse_line(line)
        if not any(
            cube_set for cube_set in cube_sets if cube_set.get("is_valid") is False
        ):
            result += game_id
    return result


def solution2(data):
    min_cubes_per_color = []
    for line in data:
        (_, cube_sets) = _parse_line(line)

        min_cube_set_for_valid_game = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for cube_set in cube_sets:
            for cube_color, cubes_number in cube_set.items():
                if cube_color != "is_valid":
                    if min_cube_set_for_valid_game[cube_color] < cubes_number:
                        min_cube_set_for_valid_game[cube_color] = cubes_number

        min_cubes_per_color.append(
            prod(
                value
                for value in min_cube_set_for_valid_game.values()
                if value > 0 or value is not False
            )
        )

    return sum(min_cubes_per_color)


def _parse_line(line):
    split_line = line.split(":")
    game_id = int(re.findall("[0-9]+", split_line[0])[0])
    cubes_sets = split_line[1].split(";")
    parsed_cube_sets = [create_cube_set(cube_set) for cube_set in cubes_sets]
    return game_id, parsed_cube_sets


def create_cube_set(cube_set):
    new_cube_set = {}
    for cubes in cube_set.split(","):
        cubes_number, cube_color = cubes.strip().split(" ")
        new_cube_set[cube_color] = int(cubes_number)

        if int(cubes_number) > LIMITS[cube_color]:
            new_cube_set["is_valid"] = False
    return new_cube_set


def main(file_name="sample.txt", part=1):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = ReadFile(dir_path + "/" + file_name).get_data_from_line()

    if part == 1:
        return solution1(data)
    elif part == 2:
        return solution2(data)


if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")
