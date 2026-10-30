import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionA.D_parenthesis.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["()"], 7, id="example1"),
        param(["()()"], 17, id="example2"),
        param(["(())"], 21, id="example3"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
