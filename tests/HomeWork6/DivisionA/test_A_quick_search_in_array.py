import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionB.A_quick_search_in_array.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "10 1 10 3 4",
                "4",
                "1 10",
                "2 9",
                "3 4",
                "2 2",
            ],
            [5, 2, 2, 0],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
