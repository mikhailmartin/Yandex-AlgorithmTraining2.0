import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionA.B_multigraph import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["3 5", "1 1", "1 3", "2 1", "1 2", "2 3"],
            (3, 3, {(1, 2), (1, 3), (2, 3)}),
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
