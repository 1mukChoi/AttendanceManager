from unittest import mock
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from attendance import Attendance
from player import Player


def test_init():
    attendance = Attendance()

    assert attendance.player_index_dict == {}
    assert attendance.player_list == []


def test_add_member():
    name_list = ["Kevin", "Sunny", "James", "Steven"]
    attendance = Attendance()
    for index, name in enumerate(name_list):
        attendance.add_player(name)

        assert attendance.player_index_dict[name] == index
        assert len(attendance.player_list) == index + 1

    assert attendance.player_index_dict == {"Kevin": 0, "Sunny": 1, "James": 2, "Steven": 3}


def test_get_players():
    name_list = ["Kevin", "Sunny", "James", "Steven"]
    attendance = Attendance()
    for name in name_list:
        attendance.add_player(name)

    assert attendance.get_player("Kevin").name == "Kevin"
    assert attendance.get_player("Sunny").name == "Sunny"
    assert attendance.get_player("James").name == "James"
    assert attendance.get_player("Steven").name == "Steven"


def test_get_new_player():
    attendance = Attendance()

    assert attendance.player_list == []
    assert attendance.get_player("Kevin").name == "Kevin"
    assert len(attendance.player_list) == 1
    assert attendance.player_index_dict == {"Kevin": 0}
