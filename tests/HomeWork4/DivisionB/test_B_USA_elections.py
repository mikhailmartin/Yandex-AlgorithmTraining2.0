import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionB.B_USA_elections.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "McCain 10",
                "McCain 5",
                "Obama 9",
                "Obama 8",
                "McCain 1",
            ],
            [
                ("McCain", 16),
                ("Obama", 17),
            ],
            id="example1",
        ),
        param(
            [
                "ivanov 100",
                "ivanov 500",
                "ivanov 300",
                "petr 70",
                "tourist 1",
                "tourist 2",
            ],
            [
                ("ivanov", 900),
                ("petr", 70),
                ("tourist", 3),
            ],
            id="example2",
        ),
        param(
            [
                "bur 1",
            ],
            [
                ("bur", 1),
            ],
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
