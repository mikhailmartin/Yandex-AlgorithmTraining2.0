import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionA.E_grass.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["0 0 5 4", "4 0 3"], 14, id="example1"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
