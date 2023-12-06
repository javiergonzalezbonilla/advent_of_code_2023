
# check if directory exists 

DIRECTORY_PATH="./advent_of_code_2023/$1"

echo $DIRECTORY_PATH
if [ -e $DIRECTORY_PATH ]; then 
echo "Directory exists. Aborting" 
else 

mkdir $DIRECTORY_PATH
touch "$DIRECTORY_PATH/__init__.py"
touch "$DIRECTORY_PATH/description.txt"
touch "$DIRECTORY_PATH/input.txt"
touch "$DIRECTORY_PATH/sample.txt"

echo '# -*- coding: utf-8 -*-
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
    print(f"Result: {result}")' >  "$DIRECTORY_PATH/solution.py" 



echo 'from unittest import TestCase


class DayXSolutionTestCase(TestCase):
    def test_sample(self):
        pass

    def test_input(self):
        pass' > "./tests/test_$1.py"

echo "Creating template " 
fi
