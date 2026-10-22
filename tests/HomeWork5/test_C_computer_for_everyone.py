import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionB.C_computer_for_everyone import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 1", "1", "2"], (1, [1]), id="example1"),
        param(["1 1", "1", "1"], (0, [0]), id="example2"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
