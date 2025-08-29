import pytest
from pytest_mock import MockerFixture

from player import Player


@pytest.fixture
def make_member():
    return Player("Kevin")


def test_member_init(make_member):
    member = make_member
    assert member.name == "Kevin"
    assert member.id == Player.LAST_ID
    assert member._points == 0
    assert member._grader.grade == "NORMAL"
    assert member.attend_num == {"monday": 0,
                                 "tuesday": 0,
                                 "wednesday": 0,
                                 "thursday": 0,
                                 "friday": 0,
                                 "saturday": 0,
                                 "sunday": 0}


@pytest.mark.parametrize("attendance_day",
                         ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
def test_attend(make_member, attendance_day):
    member = make_member
    member.attend(attendance_day)
    assert member.attend_num[attendance_day] == 1


@pytest.mark.parametrize("points, grade",
                         [(0, "NORMAL"), (10, "NORMAL"), (20, "NORMAL"), (30, "SILVER"), (40, "SILVER"), (50, "GOLD"),
                          (100, "GOLD")])
def test_update_grade(make_member, points, grade, mocker: MockerFixture):
    member = make_member
    mocked_calc_points = mocker.patch("player.Player._calc_points")
    member._points = points
    mocked_print = mocker.patch("builtins.print")

    member.update_grade()

    assert member._grader.grade == grade
    mocked_calc_points.assert_called_once()
    mocked_print.assert_called_with(
        f"NAME : {member.name}, POINT : {member.total_points}, GRADE : {member._grader.grade}")


@pytest.mark.parametrize("attend_num_wednesday, attend_num_saturday, attend_num_sunday, bonus_points",
                         [(0, 9, 0, 0), (9, 9, 0, 0), (9, 0, 9, 0), (19, 9, 0, 10), (19, 9, 9, 20), (9, 19, 0, 10),
                          (19, 0, 19, 20), (119, 119, 0, 20)])
def test_check_bonus_points(make_member, attend_num_wednesday, attend_num_saturday, attend_num_sunday, bonus_points):
    member = make_member
    member.attend_num["wednesday"] = attend_num_wednesday
    member.attend_num["saturday"] = attend_num_saturday
    member.attend_num["sunday"] = attend_num_sunday

    member._check_bonus_points()

    assert member._bonus_points == bonus_points


@pytest.mark.parametrize("points, bonus_points, total_points", [(0, 9, 9), (19, 29, 48), (10, 20, 30)])
def test_total_points(make_member, points, bonus_points, total_points):
    member = make_member
    member._points = points
    member._bonus_points = bonus_points

    assert member.total_points == total_points


@pytest.mark.parametrize("is_removed_grade, attend_num_wednesday, attend_num_weekend, result",
                         [(False, 0, 0, False), (False, 10, 0, False), (False, 0, 10, False), (False, 10, 10, False),
                          (False, 0, 0, False), (False, 10, 0, False), (False, 0, 10, False), (False, 10, 10, False),
                          (True, 0, 0, True), (True, 10, 0, False), (True, 0, 10, False), (True, 10, 10, False)])
def test_is_player_removed(make_member, is_removed_grade, attend_num_wednesday, attend_num_weekend, result,
                           mocker: MockerFixture):
    member = make_member
    mocker.patch("grader.GraderNormal.is_removed", return_value=is_removed_grade)
    member.attend_num["wednesday"] = attend_num_wednesday
    member.attend_num["saturday"] = int(attend_num_weekend / 2)
    member.attend_num["sunday"] = attend_num_weekend - member.attend_num["saturday"]

    assert member.is_player_removed() == result


@pytest.mark.parametrize("attend_num, points", [
    ({"monday": 1,
      "tuesday": 0,
      "wednesday": 0,
      "thursday": 0,
      "friday": 0,
      "saturday": 0,
      "sunday": 0}, 1),
    ({"monday": 0,
      "tuesday": 0,
      "wednesday": 10,
      "thursday": 0,
      "friday": 0,
      "saturday": 0,
      "sunday": 0}, 40),
    ({"monday": 0,
      "tuesday": 0,
      "wednesday": 0,
      "thursday": 0,
      "friday": 0,
      "saturday": 10,
      "sunday": 0}, 30),
    ({"monday": 0,
      "tuesday": 0,
      "wednesday": 0,
      "thursday": 0,
      "friday": 0,
      "saturday": 0,
      "sunday": 10}, 30)
])
def test_calc_points(make_member, attend_num, points):
    member = make_member

    member.attend_num = attend_num

    member._calc_points()

    assert member.total_points == points
