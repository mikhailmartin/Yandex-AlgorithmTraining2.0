import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionA.B_tickets.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["1 10 0 5 5"], 1, id="example1"),
        param(["10 100 50 50 5"], 9, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
