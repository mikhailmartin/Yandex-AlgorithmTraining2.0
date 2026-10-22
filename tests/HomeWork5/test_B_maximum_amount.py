import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionB.B_maximum_amount import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4", "1 2 3 4"], 10, id="example1"),
        param(["4", "5 4 -10 4"], 9, id="example2"),
        param(["4", "-1 -1 10 -1"], 10, id="custom1"),
        param(["4", "-1 -1 -1 -1"], -1, id="custom2"),
        param(["4", "-4 -3 -2 -1"], -1, id="custom3"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
