import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionB.C_genealogy_LCA.main import main


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
                "Alexander_I Nicholaus_I",
                "Peter_II Paul_I",
                "Alexander_I Anna",
            ],
            ["Paul_I", "Peter_I", "Anna"],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
