import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionA.E_names.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["abcabca", "abcda"], "ca", id="example1"),
        param(["ccba", "accbbaa"], "ccba", id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
