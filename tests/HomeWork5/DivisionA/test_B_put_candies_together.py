import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionA.B_put_candies_together.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "2 2",
                "3 2",
                "2 1",
            ],
            [11, 1],
            id="example1",
        ),
        param(
            [
                "1",
                "1 7",
            ],
            [7],
            id="example2",
        ),
        param(
            [
                "5",
                "1 1",
                "2 1",
                "3 1",
                "4 1",
                "5 2",
            ],
            [15, 5],
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
