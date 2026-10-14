import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionB.B_has_number_appeared_before import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["1 2 3 2 3 4"],
            ["NO", "NO", "NO", "YES", "YES", "NO"],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
