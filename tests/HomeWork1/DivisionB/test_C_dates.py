import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionB.C_dates import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 2 2003"], 0, id="example1"),
        param(["2 29 2008"], 1, id="example2"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
