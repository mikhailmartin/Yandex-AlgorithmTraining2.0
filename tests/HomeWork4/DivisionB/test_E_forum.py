import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork4.DivisionB.E_forum import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "7",
                "0",
                "Олимпиада по информатике",
                "Скоро третья командная олимпиада?",
                "0",
                "Новая компьютерная игра",
                "Вышла новая крутая игра!",
                "1",
                "Она пройдет 24 ноября",
                "1",
                "В Санкт-Петербурге и Барнауле",
                "2",
                "Где найти?",
                "4",
                "Примет участие более 50 команд",
                "6",
                "Интересно, какие будут задачи",
            ],
            "Олимпиада по информатике",
            id="example1",
        ),
        param(
            [
                "1",
                "0",
                "topic 1",
                "body 1",
            ],
            "topic 1",
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    assert main(lines) == expected
