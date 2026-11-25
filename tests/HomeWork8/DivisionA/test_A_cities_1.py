import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.DivisionA.A_cities_1.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["2", "1 2"],
            (1, 2, 1, 2),
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
