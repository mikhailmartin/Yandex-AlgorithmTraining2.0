import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionB.A_TolyaCarp_and_new_set_of_structures_part_2.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "7",
                "1 5",
                "10 -5",
                "1 10",
                "4 -2",
                "4 3",
                "4 1",
                "4 0",
            ],
            [(1, 15), (4, 2), (10, -5)],
            id="example1",
        ),
        param(
            [
                "5",
                "5 -10000",
                "-5 100000000000",
                "10 2000000000000",
                "-5 -300000000000",
                "0 10000000000000",
            ],
            [(-5, -200000000000), (0, 10000000000000), (5, -10000), (10, 2000000000000)],
            id="example2",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
