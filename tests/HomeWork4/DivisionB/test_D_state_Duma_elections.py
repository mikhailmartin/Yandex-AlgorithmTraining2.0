import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionB.D_state_Duma_elections.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "Party One 100000",
                "Party Two 200000",
                "Party Three 400000",
            ],
            [
                ("Party One", 64),
                ("Party Two", 129),
                ("Party Three", 257),
            ],
            id="example1",
        ),
        param(
            [
                "Party number one 100",
                "Partytwo 100",
            ],
            [
                ("Party number one", 225),
                ("Partytwo", 225),
            ],
            id="example2",
        ),
        param(
            [
                "Party number one 449",
                "Partytwo 1",
            ],
            [
                ("Party number one", 449),
                ("Partytwo", 1),
            ],
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
