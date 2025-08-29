import pytest
from pytest_mock import MockerFixture

from mission2.member import Member


def test_member_init():
    member = Member("Kevin")
    assert member.name == "Kevin"
    assert member.id == Member.LAST_ID
    assert member.points == 0
    assert member.grade == "NORMAL"
    assert member.attend_num_wednesday == 0
    assert member.attend_num_weekend == 0

@pytest.mark.parametrize("attendance_day, points, attend_num_wednesday, attend_num_weekend", [("monday", 1, 0, 0), ("tuesday", 1, 0, 0), ("wednesday", 3, 1, 0), ("thursday", 1, 0, 0), ("friday", 1, 0, 0), ("saturday", 2, 0, 1), ("sunday", 2, 0, 1)])
def test_attend(attendance_day, points, attend_num_wednesday, attend_num_weekend):
    member = Member("Kevin")
    member.attend(attendance_day)
    assert member.points == points
    assert member.attend_num_wednesday == attend_num_wednesday
    assert member.attend_num_weekend == attend_num_weekend


@pytest.mark.parametrize("points, grade", [(0, "NORMAL"), (10, "NORMAL"), (20, "NORMAL"), (30, "SILVER"), (40, "SILVER"), (50, "GOLD"), (100, "GOLD")])
def test_update_grade(points, grade, mocker: MockerFixture):
    member = Member("Kevin")
    member.points = points
    mocked_print = mocker.patch("builtins.print")

    member.update_grade()

    assert member.grade == grade
    mocked_print.assert_called_with(f"NAME : {member.name}, POINT : {member.points}, GRADE : {member.grade}")