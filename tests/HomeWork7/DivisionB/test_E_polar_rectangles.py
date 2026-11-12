import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionB.E_polar_rectangles.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["2", "1 3 0 3", "2 4 1.5 4.5"], 3.75, id="example1"),
        param(["2", "1 2 0 3", "1 2 2 1"], 3.0, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
