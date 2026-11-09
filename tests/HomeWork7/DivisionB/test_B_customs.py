import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionB.B_customs.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "3 2",
                "4 2",
                "5 2",
            ],
            2,
            id="example1",
        ),
        param(
            [
                "5",
                "13 4",
                "15 1",
                "11 5",
                "12 3",
                "10 3",
            ],
            3,
            id="example2",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
