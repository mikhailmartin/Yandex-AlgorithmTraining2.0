import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionB.C_root_of_cubic_equation.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 -3 3 -1"], 1.0000036491, id="example1"),
        param(["-1 -6 -12 -7"], -1.0000000111, id="example2"),
    ],
)
def test_main(lines, expected):
    assert abs(main(lines) - expected) < 1e6
