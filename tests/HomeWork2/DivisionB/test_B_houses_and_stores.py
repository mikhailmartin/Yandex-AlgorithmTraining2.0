import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionB.B_houses_and_stores import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["2 0 1 1 0 1 0 2 1 2"], 3, id="example1"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
