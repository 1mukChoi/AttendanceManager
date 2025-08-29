from mission2.member import Member


def test_member_init():
    member = Member("Kevin")
    assert member.name == "Kevin"
    assert member.id == Member.LAST_ID
    assert member.points == 0
    assert member.grade == "NORMAL"
    assert member.attend_num_wednesday == 0
    assert member.attend_num_weekend == 0