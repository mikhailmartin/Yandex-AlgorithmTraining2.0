import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.DivisionA.D_Petya_Masha_and_ropes.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["4", "1 5 2 1"], 1, id="example1"),
        param(["4", "5 12 4 3"], 24, id="example2"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
