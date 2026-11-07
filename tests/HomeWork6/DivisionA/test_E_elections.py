import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionA.E_elections.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3", "7 -1", "2 8", "1 2"], (6, 3, [3, 2, 5]), id="example"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
