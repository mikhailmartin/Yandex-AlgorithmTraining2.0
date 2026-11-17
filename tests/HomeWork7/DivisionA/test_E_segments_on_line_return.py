import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork7.DivisionA.E_segments_on_line_return.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "2 3",
                "0 4",
                "1 6",
                "0 5",
            ],
            [3, 4, 0, 0],
            id="example",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
