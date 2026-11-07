import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionB.E_coverage_by_K_segments.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["6 2", "1 2 3 9 8 7"], 2, id="example"),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
