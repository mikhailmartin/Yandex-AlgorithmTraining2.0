import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionA.E_another_pair_of_triangles import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3"], ((1, 1, 1), (1, 1, 1)), id="example1"),
        param(["4"], -1, id="example2"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
