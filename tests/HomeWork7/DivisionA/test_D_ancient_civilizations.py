import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionA.D_ancient_civilizations.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "-600 -400",
                "-450 -300",
                "-400 -50",
            ],
            (1, 2),
            id="example1",
        ),
        param(
            [
                "2",
                "10 20",
                "15 21",
            ],
            (1, 2),
            id="example2",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
