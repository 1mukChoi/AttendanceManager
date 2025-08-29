import pytest
from pytest_mock import MockerFixture

from attendance import Attendance


def test_init():
    attendance = Attendance()

    assert attendance.player_index_dict == {}
    assert attendance.player_list == []


def test_add_member(mocker: MockerFixture):
    name_list = ["Kevin", "Sunny", "James", "Steven"]
    mocker.patch('player.Player', return_value=name_list)
    attendance = Attendance()
    for index, name in enumerate(name_list):
        attendance.add_player(name)

        assert attendance.player_index_dict[name] == index
        assert len(attendance.player_list) == index + 1

    assert attendance.player_index_dict == {"Kevin": 0, "Sunny": 1, "James": 2, "Steven": 3}