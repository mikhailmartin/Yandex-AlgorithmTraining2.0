import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionA.D_bureaucracy.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3", "1 1"], [5, 1, 1], id="example1"),
        param(["5", "1 2 2 4"], [13, 8, 1, 3, 1], id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
