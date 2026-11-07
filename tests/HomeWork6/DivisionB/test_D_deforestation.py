import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionB.D_deforestation.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 2 1 3 10"], 8, id="example1"),
        param(["1 2 1 3 11"], 9, id="example2"),
        param(["19 3 14 6 113"], 4, id="example3"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
