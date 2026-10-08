import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionA.D_Futurama import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["4 1", "1 2"],
            [(1, 3), (2, 4), (1, 4), (2, 3), (3, 4)],
            id="example1",
        ),
        param(
            ["5 1", "1 2"],
            [(1, 4), (2, 5), (1, 5), (2, 4), (4, 5)],
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
