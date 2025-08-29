from mission2.member import Member


class Attendance:
    def __init__(self):
        self.member_index_dict = {}
        self.member_list: list[Member] = []

    def add_member(self, name):
        new_member = Member(name)
        new_member_index = len(self.member_list)

        self.member_index_dict[name] = new_member_index
        self.member_list.append(new_member)


    def get_member(self, name):
        if name not in self.member_index_dict:
            self.add_member(name)

        return self.member_list[self.member_index_dict[name]]


    def check_bonus_points(self):
        for member in self.member_list:
            if member.attend_num_wednesday > 9:
                member.points += 10
            if member.attend_num_weekend > 9:
                member.points += 10


    def get_grade(self):
        for member in self.member_list:
            if member.points >= 50:
                member.grade = "GOLD"
            elif member.points >= 30:
                member.grade = "SILVER"
            else:
                member.grade = "NORMAL"

            print(f"NAME : {member.name}, POINT : {member.points}, GRADE : {member.grade}")


    def remove_player(self):
        print("\nRemoved player")
        print("==============")
        for member in self.member_list:
            if member.grade in ("GOLD", "SILVER"):
                continue
            if member.attend_num_wednesday != 0:
                continue
            if member.attend_num_weekend != 0:
                continue
            print(member.name)


    def input_attendance_data(self, read_data):
        for data in read_data:
            parts = data.strip().split()
            if len(parts) != 2:
                continue

            member = self.get_member(name=parts[0])
            member.attend(attendance_day=parts[1])

        self.check_bonus_points()

def open_input_file():
    read_file = []
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        for _ in range(500):
            line = f.readline()
            if not line:
                break
            read_file.append(line)

    return read_file


def main():
    try:
        attendance_data = open_input_file()

        attendance = Attendance()
        attendance.input_attendance_data(attendance_data)

        attendance.get_grade()

        attendance.remove_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
