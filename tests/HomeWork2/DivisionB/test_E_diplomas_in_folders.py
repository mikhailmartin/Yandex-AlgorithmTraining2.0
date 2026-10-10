import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionB.E_diplomas_in_folders import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["2", "2 1"], 1, id="example1"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
