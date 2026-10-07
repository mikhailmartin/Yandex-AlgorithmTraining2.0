import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionB.B_circle_line_of_metro import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["100 5 6"], 0, id="example1"),
        param(["10 1 9"], 1, id="example2"),
        param(["100 6 5"], 0, id="custom1"),
        param(["10 9 1"], 1, id="custom2"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
