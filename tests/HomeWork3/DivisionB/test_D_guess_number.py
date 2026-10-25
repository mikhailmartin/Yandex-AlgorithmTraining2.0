import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionB.D_guess_number.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "10",
                "1 2 3 4 5",
                "YES",
                "2 4 6 8 10",
                "NO",
                "HELP",
            ],
            [1, 3, 5],
            id="example1",
        ),
        param(
            [
                "10",
                "1 2 3 4 5 6 7 8 9 10",
                "YES",
                "1",
                "NO",
                "2",
                "NO",
                "3",
                "NO",
                "4",
                "NO",
                "6",
                "NO",
                "7",
                "NO",
                "8",
                "NO",
                "9",
                "NO",
                "10",
                "NO",
                "HELP",
            ],
            [5],
            id="example2",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
