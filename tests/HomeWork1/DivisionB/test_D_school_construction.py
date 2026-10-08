import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionB.D_school_construction import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4", "1 2 3 4"], 3, id="example1"),
        param(["3", "-1 0 1"], 0, id="example2"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
