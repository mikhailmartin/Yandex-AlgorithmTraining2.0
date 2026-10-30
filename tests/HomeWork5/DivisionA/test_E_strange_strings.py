import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork5.DivisionA.E_strange_strings.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["ab"], 3, id="example"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
