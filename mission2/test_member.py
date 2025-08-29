import pytest

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