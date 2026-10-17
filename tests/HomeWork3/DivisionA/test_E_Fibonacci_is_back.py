import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionA.E_Fibonacci_is_back import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["8", "1", "2", "3", "4", "5", "6", "7", "8"],
            ["Yes", "Yes", "Yes", "No", "Yes", "No", "No", "Yes"],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
