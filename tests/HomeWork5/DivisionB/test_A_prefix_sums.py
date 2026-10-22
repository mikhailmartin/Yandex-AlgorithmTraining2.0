import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionB.A_prefix_sums import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4 10",
                "1 2 3 4",
                "1 1",
                "1 2",
                "1 3",
                "1 4",
                "2 2",
                "2 3",
                "2 4",
                "3 3",
                "3 4",
                "4 4",
            ],
            [1, 3, 6, 10, 2, 5, 9, 3, 7, 4],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
