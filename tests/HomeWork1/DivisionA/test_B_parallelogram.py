import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionA.B_parallelogram import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "1 1 4 2 3 0 2 3",
                "1 1 5 2 2 3 3 0",
                "0 0 5 1 6 3 1 2",
            ],
            ["YES", "NO", "YES"],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
