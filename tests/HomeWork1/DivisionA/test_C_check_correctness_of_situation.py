import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.DivisionA.C_check_correctness_of_situation import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "1 1 1",
                "1 1 1",
                "1 1 1",
            ],
            "NO",
            id="example1",
        ),
        param(
            [
                "2 1 1",
                "1 1 2",
                "2 2 1",
            ],
            "YES",
            id="example2",
        ),
        param(
            [
                "1 1 1",
                "2 0 2",
                "0 0 0",
            ],
            "YES",
            id="example3",
        ),
        param(
            [
                "0 0 0",
                "0 1 0",
                "0 0 0",
            ],
            "YES",
            id="example4",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
