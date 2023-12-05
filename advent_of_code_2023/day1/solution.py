# -*- coding: utf-8 -*-

import os

from ..utils import ReadFile


def solution(data):
    data_length = len(data)
    print(data_length)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = ReadFile(dir_path + "/input.txt").get_data_separated_by_breakline()
    solution(data)
