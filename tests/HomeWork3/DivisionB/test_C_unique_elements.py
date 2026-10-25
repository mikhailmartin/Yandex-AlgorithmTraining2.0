import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionB.C_unique_elements.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 2 2 3 3 3"], ["1"], id="example1"),
        param(["4 3 5 2 5 1 3 5"], ["4", "2", "1"], id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
