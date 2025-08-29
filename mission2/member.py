class Member:
    LAST_ID = 0
    def __init__(self, name = None):
        Member.LAST_ID += 1
        self.name = name
        self.id = Member.LAST_ID
        self.points = 0
        self.grade = "NORMAL"
        self.attend_num_wednesday = 0
        self.attend_num_weekend = 0