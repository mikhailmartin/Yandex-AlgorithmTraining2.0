import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork6.DivisionA.C_passing_score_for_olympiad.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "9 6 5",
                "6 1 799 0",
                "2 4 995 0",
                "1 4 989 1",
                "7 2 538 0",
                "5 4 984 0",
                "8 2 1000 0",
                "3 2 998 0",
                "4 2 823 1",
                "9 1 543 0",
            ],
            985,
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
