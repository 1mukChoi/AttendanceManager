from unittest import mock
from unittest.mock import Mock, call

import pytest
from pytest_mock import MockerFixture

from attendance import Attendance
from player import Player


@pytest.fixture
def basic_attendance():
    name_list = ["Kevin", "Sunny", "James", "Steven"]
    attendance = Attendance()
    for name in name_list:
        attendance.add_player(name)
    return attendance


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


def test_get_players(basic_attendance):
    attendance = basic_attendance

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


def test_manage_players(basic_attendance, mocker: MockerFixture):
    attendance = basic_attendance
    mocked_update_grade = mocker.patch("player.Player.update_grade")
    mocked_is_player_removed = mocker.patch("player.Player.is_player_removed", side_effect=[True, False, False, False])
    mocked_print = mocker.patch("builtins.print")

    attendance.manage_players()

    assert mocked_update_grade.call_count == len(attendance.player_list)
    assert mocked_is_player_removed.call_count == len(attendance.player_list)
    assert mocked_print.call_count == 3
    mocked_print.assert_has_calls([call("\nRemoved player"),
                                   call("=============="),
                                   call(f"{attendance.player_list[0].name}"),
                                   ])


def test_input_attendance_data(mocker: MockerFixture):
    attendance = Attendance()
    input_data = ["Umar monday", "Daisy tuesday", "Alice tuesday"]
    mocked_player = mock.Mock(spec=Player)
    mocked_open_input_file = mocker.patch("attendance.Attendance.open_input_file", return_value=input_data)
    mocked_get_player = mocker.patch("attendance.Attendance.get_player", return_value=mocked_player)
    mocker.patch("player.Player.attend")

    attendance.input_attendance_data("example.txt")

    mocked_open_input_file.assert_called_once()
    assert mocked_get_player.call_count == len(input_data)
    mocked_get_player.assert_has_calls([call(name="Umar"), call(name="Daisy"), call(name="Alice")])
    assert mocked_player.attend.call_count == len(input_data)
    mocked_player.attend.assert_has_calls(
        [call(attendance_day="monday"), call(attendance_day="tuesday"), call(attendance_day="tuesday")])


def test_input_attendance_wrong_data(mocker: MockerFixture):
    attendance = Attendance()
    input_data = ["Umar monday", "Daisy", "Alice tuesday"]
    mocked_player = mock.Mock(spec=Player)
    mocked_open_input_file = mocker.patch("attendance.Attendance.open_input_file", return_value=input_data)
    mocked_get_player = mocker.patch("attendance.Attendance.get_player", return_value=mocked_player)
    mocker.patch("player.Player.attend")

    attendance.input_attendance_data("example.txt")

    mocked_open_input_file.assert_called_once()
    assert mocked_get_player.call_count == len(input_data) - 1
    mocked_get_player.assert_has_calls([call(name="Umar"), call(name="Alice")])
    assert mocked_player.attend.call_count == len(input_data) - 1
    mocked_player.attend.assert_has_calls([call(attendance_day="monday"), call(attendance_day="tuesday")])

