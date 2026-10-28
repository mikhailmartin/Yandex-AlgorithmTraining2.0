import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionA.C_best_friends_fullerenes.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4", "2 2 3 4"], 3, id="example"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
