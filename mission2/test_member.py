from pickle import FALSE
from xmlrpc.client import Fault

import pytest
from pytest_mock import MockerFixture

from mission2.player import Player

@pytest.fixture
def make_member():
    return Player("Kevin")

def test_member_init(make_member):
    member = make_member
    assert member.name == "Kevin"
    assert member.id == Player.LAST_ID
    assert member._points == 0
    assert member.grade == "NORMAL"
    assert member.attend_num_wednesday == 0
    assert member.attend_num_weekend == 0

@pytest.mark.parametrize("attendance_day, points, attend_num_wednesday, attend_num_weekend", [("monday", 1, 0, 0), ("tuesday", 1, 0, 0), ("wednesday", 3, 1, 0), ("thursday", 1, 0, 0), ("friday", 1, 0, 0), ("saturday", 2, 0, 1), ("sunday", 2, 0, 1)])
def test_attend(make_member, attendance_day, points, attend_num_wednesday, attend_num_weekend):
    member = make_member
    member.attend(attendance_day)
    assert member._points == points
    assert member.attend_num_wednesday == attend_num_wednesday
    assert member.attend_num_weekend == attend_num_weekend


@pytest.mark.parametrize("points, grade", [(0, "NORMAL"), (10, "NORMAL"), (20, "NORMAL"), (30, "SILVER"), (40, "SILVER"), (50, "GOLD"), (100, "GOLD")])
def test_update_grade(make_member, points, grade, mocker: MockerFixture):
    member = make_member
    member._points = points
    mocked_print = mocker.patch("builtins.print")
    mocked_check_bonus_points = mocker.patch("mission2.player.Player._check_bonus_points")

    member.update_grade()

    assert member.grade == grade
    mocked_print.assert_called_with(f"NAME : {member.name}, POINT : {member.total_points}, GRADE : {member.grade}")
    mocked_check_bonus_points.assert_called_once()


@pytest.mark.parametrize("attend_num_wednesday, attend_num_weekend, bonus_points", [(0, 9, 0), (9, 9, 0), (9, 0, 0), (19, 9, 10), (9, 19, 10), (19, 19, 20), (119, 119, 20)])
def test_check_bonus_points(make_member, attend_num_wednesday, attend_num_weekend, bonus_points):
    member = make_member
    member.attend_num_wednesday = attend_num_wednesday
    member.attend_num_weekend = attend_num_weekend

    member._check_bonus_points()

    assert member._bonus_points == bonus_points

@pytest.mark.parametrize("points, bonus_points, total_points", [(0, 9, 9), (19, 29, 48), (10, 20, 30)])
def test_total_points(make_member, points, bonus_points, total_points):
    member = make_member
    member._points = points
    member._bonus_points = bonus_points

    assert member.total_points == total_points

@pytest.mark.parametrize("grade, attend_num_wednesday, attend_num_weekend, result", [("GOLD", 0, 0, False), ("GOLD", 10, 0, False), ("GOLD", 0, 10, False), ("GOLD", 10, 10, False),
                                                                                     ("SILVER", 0, 0, False), ("SILVER", 10, 0, False), ("SILVER", 0, 10, False), ("SILVER", 10, 10, False),
                                                                                     ("NORMAL", 0, 0, True), ("NORMAL", 10, 0, False), ("NORMAL", 0, 10, False), ("NORMAL", 10, 10, False)])
def test_is_player_removed(make_member, grade, attend_num_wednesday, attend_num_weekend, result):
    member = make_member
    member.grade = grade
    member.attend_num_wednesday = attend_num_wednesday
    member.attend_num_weekend = attend_num_weekend

    assert member.is_player_removed() == result