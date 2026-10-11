import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionA.B_inventive_Petya import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["mama", "amamam"], "m", id="example1"),
        param(["ura", "mura"], "mura", id="example2"),
        param(["computer", "comp"], "comp", id="example3"),
        param(["ejudge", "judge"], "", id="example4"),
        param(["m", "mmm"], "", id="example5"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
