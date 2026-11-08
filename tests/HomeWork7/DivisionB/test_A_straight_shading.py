import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionB.A_straight_shading.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1", "10 20"], 10, id="example1"),
        param(["1", "10 10"], 0, id="example2"),
        param(["2", "10 20", "20 40"], 30, id="example3"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
