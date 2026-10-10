import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionB.D_benches_in_atrium import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["5 2", "0 2"], [2], id="example1"),
        param(["13 4", "1 4 8 11"], [4, 8], id="example2"),
        param(["14 6", "1 6 8 11 12 13"], [6, 8], id="example3"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
