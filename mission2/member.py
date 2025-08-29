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

    def attend(self, attendance_day):
        if attendance_day == "wednesday":
            self.points += 3
            self.attend_num_wednesday += 1
        elif attendance_day == "saturday":
            self.points += 2
            self.attend_num_weekend += 1
        elif attendance_day == "sunday":
            self.points += 2
            self.attend_num_weekend += 1
        else:
            self.points += 1


    def update_grade(self):
        if self.points >= 50:
            self.grade = "GOLD"
        elif self.points >= 30:
            self.grade = "SILVER"
        else:
            self.grade = "NORMAL"

        print(f"NAME : {self.name}, POINT : {self.points}, GRADE : {self.grade}")

