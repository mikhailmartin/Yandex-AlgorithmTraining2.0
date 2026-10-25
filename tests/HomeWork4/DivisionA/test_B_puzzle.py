import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionA.B_puzzle.main import main

from collections import Counter


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5 3",
                "POLTE",
                "RWYMS",
                "OAIPT",
                "BDANR",
                "LEMES",
                "OLYMPIAD",
                "PROBLEM",
                "TEST",
            ],
            Counter("AENRSW"),
            id="example1",
        ),
    ],
)
def test_soltest_mainve(lines, expected):
    assert main(lines) == expected
