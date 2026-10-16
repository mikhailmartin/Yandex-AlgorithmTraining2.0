import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionA.C_strikes import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["19 3", "2 3", "3 5", "9 8"], 8, id="example1"),
        param(["5 2", "1 2", "2 2"], 5, id="example2"),
        param(["1000 1", "1 1"], 715, id="example3"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
