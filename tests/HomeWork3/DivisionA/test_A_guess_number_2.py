import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionA.A_guess_number_2.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "10",
                "1 2 3 4 5",
                "2 4 6 8 10",
                "HELP",
            ],
            (["NO", "YES"], [6, 8, 10]),
            id="example1",
        ),
        param(
            [
                "10",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "HELP",
            ],
            (["NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO"], [10]),
            id="example2",
        ),
        param(
            [
                "16",
                "1 2 3 4 5 6 7 8",
                "9 10 11 12",
                "13 14",
                "16",
                "HELP",
            ],
            (["NO", "NO", "NO", "NO"], [15]),
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
