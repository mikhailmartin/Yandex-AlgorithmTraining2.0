import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionA.C_union_of_rectangles.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "1 1 3 5",
                "5 2 7 4",
                "2 4 6 7",
            ],
            23,
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
