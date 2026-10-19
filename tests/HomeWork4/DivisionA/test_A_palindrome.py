import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionA.A_palindrome import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(["3", "AAB"], "ABA", id="example1"),
        param(["6", "QAZQAZ"], "AQZZQA", id="example2"),
        param(["6", "ABCDEF"], "A", id="example3"),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
