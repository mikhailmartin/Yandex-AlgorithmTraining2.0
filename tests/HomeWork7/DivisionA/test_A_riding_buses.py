import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionA.A_riding_buses.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "6 4",
                "4  1 2 3 5",
                "2  3 4",
                "5  5 2 1 3 2",
                "2  4 3",
                "3",
                "1  4  1 2 3 4",
                "2  1  1",
                "6  3  1 2 3",
            ],
            [
                (20, 1),
                (2, 3),
                (0, 0),
            ],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
