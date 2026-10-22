import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionB.D_correct_round_bracketed import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["(())()"], "YES", id="example1"),
        param(["(()))()"], "NO", id="example2"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
