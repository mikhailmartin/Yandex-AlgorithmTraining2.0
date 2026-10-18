import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionB.C_frequency_analysis import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "hi",
                "hi",
                "what is your name",
                "my name is bond",
                "james bond",
                "my name is damme",
                "van damme",
                "claude van damme",
                "jean claude van damme",
            ],
            [
                "damme",
                "is",
                "name",
                "van",
                "bond",
                "claude",
                "hi",
                "my",
                "james",
                "jean",
                "what",
                "your",
            ],
            id="example1",
        ),
        param(
            [
                "oh you touch my tralala",
                "mmm my ding ding dong",
            ],
            [
                "ding",
                "my",
                "dong",
                "mmm",
                "oh",
                "touch",
                "tralala",
                "you",
            ],
            id="example2",
        ),
        param(
            [
                "ai ai ai ai ai ai ai ai ai ai",
            ],
            [
                "ai",
            ],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
