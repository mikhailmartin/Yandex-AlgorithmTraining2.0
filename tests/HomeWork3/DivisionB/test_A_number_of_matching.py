import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionB.A_number_of_matching.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 3 2", "4 3 2"], 2, id="example1"),
        param(["1 2 6 4 5 7", "10 2 3 4 8"], 2, id="example2"),
        param(["1 7 3 8 10 2 5", "6 5 2 8 4 3 7"], 5, id="example3"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
