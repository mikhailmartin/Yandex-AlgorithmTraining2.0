import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionB.C_making_palindromes import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["a"], 0, id="example1"),
        param(["ab"], 1, id="example2"),
        param(["cognitive"], 4, id="example3"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
