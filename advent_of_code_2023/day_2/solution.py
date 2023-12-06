# -*- coding: utf-8 -*-
import os

from advent_of_code_2023.utils import ReadFile


def solution(data):
    pass


def main(file_name="sample.txt"):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = ReadFile(dir_path + "/" + file_name).get_data_from_line()
    return solution(data)


if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")
