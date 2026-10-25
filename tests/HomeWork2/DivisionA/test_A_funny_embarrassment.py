import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionA.A_funny_embarrassment.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4 2", "45 52 47 46"], 7, id="example1"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
