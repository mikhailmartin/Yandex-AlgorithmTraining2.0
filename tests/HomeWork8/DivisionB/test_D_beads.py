import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionB.D_beads.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2",
                "1 2",
            ],
            2,
            id="example1",
        ),
        param(
            [
                "5",
                "2 1",
                "2 3",
                "2 4",
                "2 5",
            ],
            3,
            id="example2",
        ),
        param(
            [
                "10",
                "1 2",
                "2 3",
                "3 4 ",
                "4 5",
                "1 6",
                "6 10",
                "10 9",
                "9 8",
                "8 7",
            ],
            10,
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
