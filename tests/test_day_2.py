from unittest import TestCase
from advent_of_code_2023.day_2 import solution


class Day2SolutionPart1TestCase(TestCase):
    def test_sample(self):
        self.assertEqual(solution.main("sample.txt"), 8)

    def test_input(self):
        self.assertEqual(solution.main("input.txt"), 2447)


class Day2Solutionpart2TestCase(TestCase):
    def test_sample(self):
        self.assertEqual(solution.main("sample.txt", 2), 2286)

    def test_input(self):
        self.assertEqual(solution.main("input.txt", 2), 56322)
        pass
