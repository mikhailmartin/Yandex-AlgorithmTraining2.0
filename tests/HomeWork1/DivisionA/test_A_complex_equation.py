import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionA.A_complex_equation import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1", "1", "2", "2"], "NO", id="example1"),
        param(["2", "-4", "7", "1"], "2", id="example2"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
