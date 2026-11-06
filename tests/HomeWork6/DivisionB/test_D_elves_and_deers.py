import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionA.D_elves_and_deers.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4 6",
                "2 3 4 5",
                "1 3 2 2 5 2",
            ],
            [(1, 1, 2), (2, 4, 5)],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
