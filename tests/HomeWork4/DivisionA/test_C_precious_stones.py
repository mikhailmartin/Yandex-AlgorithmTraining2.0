import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionA.C_precious_stones import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "7 1",
                "abacaba",
                "aa",
            ],
            6,
            id="example1",
        ),
        param(
            [
                "7 3",
                "abacaba",
                "ab",
                "ac",
                "bb",
            ],
            7,
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
