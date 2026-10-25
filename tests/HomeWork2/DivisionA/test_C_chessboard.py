import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionA.C_chessboard.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3", "1 1", "1 2", "2 1"], 8, id="example1"),
        param(["1", "8 8"], 4, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
