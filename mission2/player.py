from grader import GraderBase, GraderNormal


class Player:
    LAST_ID = 0

    def __init__(self, name=None):
        Player.LAST_ID += 1
        self.name = name
        self.id = Player.LAST_ID
        self._points = 0
        self._bonus_points = 0
        self._grader: GraderBase = self._get_grader()
        self.attend_num_wednesday = 0
        self.attend_num_weekend = 0

    def _get_grader(self):
        return GraderNormal()

    def attend(self, attendance_day):
        if attendance_day == "wednesday":
            self._points += 3
            self.attend_num_wednesday += 1
        elif attendance_day == "saturday":
            self._points += 2
            self.attend_num_weekend += 1
        elif attendance_day == "sunday":
            self._points += 2
            self.attend_num_weekend += 1
        else:
            self._points += 1

    def update_grade(self):
        self._check_bonus_points()

        self._grader.set_grade(self.total_points)

        print(f"NAME : {self.name}, POINT : {self.total_points}, GRADE : {self._grader.grade}")

    def _check_bonus_points(self):
        self._bonus_points = 0
        if self.attend_num_wednesday > 9:
            self._bonus_points += 10
        if self.attend_num_weekend > 9:
            self._bonus_points += 10

    def _total_points(self):
        return self._points + self._bonus_points

    @property
    def total_points(self):
        return self._total_points()

    def is_player_removed(self):
        if not self._grader.is_removed():
            return False
        if self.attend_num_wednesday != 0:
            return False
        if self.attend_num_weekend != 0:
            return False

        return True