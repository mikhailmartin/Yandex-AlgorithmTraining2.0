import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionB.E_sum_of_three import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "2 1 2",
                "2 3 1",
                "2 3 1",
            ],
            (0, 1, 1),
            id="example1",
        ),
        param(
            [
                "10",
                "1 5",
                "1 4",
                "1 3",
            ],
            (-1,),
            id="example2",
        ),
        param(
            [
                "5",
                "4 1 2 3 4",
                "3 5 2 1",
                "4 5 3 2 2",
            ],
            (0, 1, 2),
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
