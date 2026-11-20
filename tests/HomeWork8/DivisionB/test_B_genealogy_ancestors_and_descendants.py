import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionB.B_genealogy_ancestors_and_descendants.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "9",
                "Alexei Peter_I",
                "Anna Peter_I",
                "Elizabeth Peter_I",
                "Peter_II Alexei",
                "Peter_III Anna",
                "Paul_I Peter_III",
                "Alexander_I Paul_I",
                "Nicholaus_I Paul_I",
                "Anna Nicholaus_I",
                "Peter_II Peter_I",
                "Alexei Paul_I",
            ],
            ["1", "2", "0"],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
