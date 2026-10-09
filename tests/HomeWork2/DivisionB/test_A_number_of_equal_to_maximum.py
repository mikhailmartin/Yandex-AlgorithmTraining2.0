import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionB.A_number_of_equal_to_maximum import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1", "7", "9", "0"], 1, id="example1"),
        param(["1", "3", "3", "1", "0"], 2, id="example2"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
