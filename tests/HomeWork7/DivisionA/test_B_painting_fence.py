import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionA.B_painting_fence.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["2 100", "5 10"], 5, id="example1"),
        param(["4 10", "7 8 3 5"], 2, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
