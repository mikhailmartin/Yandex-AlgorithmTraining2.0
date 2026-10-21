import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionA.D_numbers import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["280138", "798081"], "8810", id="example1"),
        param(["123", "456"], "-1", id="example2"),
        param(["00", "0"], "0", id="custom1"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
