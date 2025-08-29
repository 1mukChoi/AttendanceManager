from player import Player


class Attendance:
    def __init__(self):
        self.player_index_dict = {}
        self.player_list: list[Player] = []

    def add_player(self, name):
        new_player = Player(name)
        new_player_index = len(self.player_list)

        self.player_index_dict[name] = new_player_index
        self.player_list.append(new_player)

    def get_player(self, name):
        if name not in self.player_index_dict:
            self.add_player(name)

        return self.player_list[self.player_index_dict[name]]

    def manage_players(self):
        for player in self.player_list:
            player.update_grade()

        print("\nRemoved player")
        print("==============")
        for player in self.player_list:
            if not player.is_player_removed():
                continue
            print(player.name)

    def input_attendance_data(self, file_name):
        read_data = self.open_input_file(file_name)

        for data in read_data:
            parts = data.strip().split()
            if len(parts) != 2:
                continue

            player = self.get_player(name=parts[0])
            player.attend(attendance_day=parts[1])

    def open_input_file(self, file_name):
        read_file = []
        with open(file_name, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                read_file.append(line)

        return read_file


def main():
    try:
        attendance = Attendance()
        attendance.input_attendance_data("attendance_weekday_500.txt")

        attendance.manage_players()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
