import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionB.A_interactor import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["0", "0", "0"], 0, id="example1"),
        param(["-1", "0", "1"], 3, id="example2"),
        param(["42", "1", "6"], 6, id="example3"),
        param(["44", "7", "4"], 1, id="example4"),
        param(["1", "4", "0"], 3, id="example5"),
        param(["-3", "2", "4"], 2, id="example6"),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
