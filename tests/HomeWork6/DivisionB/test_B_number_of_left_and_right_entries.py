import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionB.B_number_of_left_and_right_entries.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "1 2 2 3",
                "4",
                "4 3 2 1",
            ],
            [(0, 0), (4, 4), (2, 3), (1, 1)],
            id="example1",
        ),
        param(
            [
                "10",
                "1 2 3 4 5 6 7 7 8 9",
                "10",
                "7 3 3 1 3 7 9 7 7 10",
            ],
            [(7, 8), (3, 3), (3, 3), (1, 1), (3, 3), (7, 8), (10, 10), (7, 8), (7, 8), (0, 0)],
            id="example2",
        ),
        param(
            [
                "10",
                "1 3 3 3 3 6 8 8 9 10",
                "10",
                "2 9 6 4 2 9 3 7 9 7",
            ],
            [(0, 0), (9, 9), (6, 6), (0, 0), (0, 0), (9, 9), (2, 5), (0, 0), (9, 9), (0, 0)],
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
