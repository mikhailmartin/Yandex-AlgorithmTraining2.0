import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionA.D_Krizhanovskys_lot import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["6", "0 0 0 0 0 0", "2 3 4 5 6"], 1, id="example1"),
        param(["6", "8 3 12 5 0 9", "2 1 3 1 4"], 2, id="example2"),
        param(["8", "0 0 0 0 0 0 0 0", "1 1 2 2 3 3 4"], 1, id="example3"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
