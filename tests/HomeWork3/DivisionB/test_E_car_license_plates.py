import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.DivisionB.E_car_license_plates import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "ABC",
                "A37",
                "BCDA",
                "2",
                "A317BD",
                "B137AC",
            ],
            ["B137AC"],
            id="example1",
        ),
        param(
            [
                "2",
                "1ABC",
                "3A4B",
                "3",
                "A143BC",
                "C143AB",
                "AAABC1",
            ],
            ["A143BC", "C143AB"],
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
