from mission2.player import Player


class Attendance:
    def __init__(self):
        self.player_index_dict = {}
        self.player_list: list[Player] = []

    def add_member(self, name):
        new_member = Player(name)
        new_member_index = len(self.player_list)

        self.player_index_dict[name] = new_member_index
        self.player_list.append(new_member)


    def get_member(self, name):
        if name not in self.player_index_dict:
            self.add_member(name)

        return self.player_list[self.player_index_dict[name]]


    def get_grade(self):
        for player in self.player_list:
            player.update_grade()

    def remove_player(self):
        print("\nRemoved player")
        print("==============")
        for player in self.player_list:
            if player.grade in ("GOLD", "SILVER"):
                continue
            if player.attend_num_wednesday != 0:
                continue
            if player.attend_num_weekend != 0:
                continue
            print(player.name)


    def input_attendance_data(self, read_data):
        for data in read_data:
            parts = data.strip().split()
            if len(parts) != 2:
                continue

            player = self.get_member(name=parts[0])
            player.attend(attendance_day=parts[1])


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
