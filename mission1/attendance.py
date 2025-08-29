player_index_dict = {}
player_list = []


def add_player(name):
    new_player_index = len(player_list)
    new_player_id = new_player_index + 1

    player_index_dict[name] = new_player_index
    new_player = {"name": name,
                  "id": new_player_id,
                  "points": 0,
                  "grade": "NORMAL",
                  "attend_num_wednesday": 0,
                  "attend_num_weekend": 0}
    player_list.append(new_player)


def get_player(name):
    if name not in player_index_dict:
        add_player(name)

    return player_list[player_index_dict[name]]


def add_attendance_points(player, attendance_day):
    if attendance_day == "wednesday":
        player["points"] += 3
        player["attend_num_wednesday"] += 1
    elif attendance_day == "saturday":
        player["points"] += 2
        player["attend_num_weekend"] += 1
    elif attendance_day == "sunday":
        player["points"] += 2
        player["attend_num_weekend"] += 1
    else:
        player["points"] += 1


def check_bonus_points():
    for player in player_list:
        if player["attend_num_wednesday"] > 9:
            player["points"] += 10
        if player["attend_num_weekend"] > 9:
            player["points"] += 10


def get_grade():
    for player in player_list:
        if player["points"] >= 50:
            player["grade"] = "GOLD"
        elif player["points"] >= 30:
            player["grade"] = "SILVER"
        else:
            player["grade"] = "NORMAL"

        print(f"NAME : {player["name"]}, POINT : {player["points"]}, GRADE : {player["grade"]}")


def remove_player():
    print("\nRemoved player")
    print("==============")
    for player in player_list:
        if player["grade"] in ("GOLD", "SILVER"):
            continue
        if player["attend_num_wednesday"] != 0:
            continue
        if player["attend_num_weekend"] != 0:
            continue
        print(player["name"])


def input_attendance_data(read_data):
    for data in read_data:
        parts = data.strip().split()
        if len(parts) != 2:
            continue

        player = get_player(name=parts[0])
        add_attendance_points(player, attendance_day=parts[1])

    check_bonus_points()

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

        input_attendance_data(attendance_data)

        get_grade()

        remove_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
