# -*- coding: utf-8 -*-

import os
import re

from advent_of_code_2023.utils import ReadFile


def solution(data):
    def find_calibration_value(signal):
        result = "".join(re.findall(r"[0-9]+", signal))
        return int(f"{result[0]}{result[-1]}")

    return sum(find_calibration_value(signal) for signal in data)


def main(file_name="sample.txt"):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = ReadFile(dir_path + "/" + file_name).get_data_from_line()
    return solution(data)


if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")
