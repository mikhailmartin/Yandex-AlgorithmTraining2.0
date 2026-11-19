import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionB.A_binary_tree.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "ADD 2",
                "ADD 3",
                "ADD 2",
                "SEARCH 2",
                "ADD 5",
                "PRINTTREE",
                "SEARCH 7",
            ],
            [
                "DONE",
                "DONE",
                "ALREADY",
                "YES",
                "DONE",
                "2",
                ".3",
                "..5",
                "NO",
            ],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
