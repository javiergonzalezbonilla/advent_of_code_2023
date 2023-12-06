from unittest import TestCase
from advent_of_code_2023.day1 import solution


class DayOneSolutionTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(solution.main("sample.txt"), 142)

    def test_input(self):
        self.assertEqual(solution.main("input.txt"), 55538)
