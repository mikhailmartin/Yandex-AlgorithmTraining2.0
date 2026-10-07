import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.E_point_and_triangle import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5", "1 1"], 0, id="example1"),
        param(["3", "-1 -1"], 1, id="example2"),
        param(["4", "4 4"], 2, id="example3"),
        param(["4", "2 2"], 0, id="example4"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
