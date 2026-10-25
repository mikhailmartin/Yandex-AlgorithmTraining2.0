import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionA.A_stylish_clothing_2.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "1 2 3",
                "2",
                "1 3",
                "2",
                "3 4",
                "2",
                "2 3",
            ],
            (3, 3, 3, 3),
            id="example1",
        ),
        param(
            [
                "1",
                "5",
                "4",
                "3 6 7 10",
                "4",
                "18 3 9 11",
                "1",
                "20",
            ],
            (5, 6, 9, 20),
            id="example2",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
