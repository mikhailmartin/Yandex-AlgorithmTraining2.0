import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionB.E_Huffman_tree.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2",
                "DUDDUU",
                "DU",
            ],
            [
                "4",
                "0",
                "100",
                "101",
                "11",
                "2",
                "0",
                "1",
            ],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
