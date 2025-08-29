member_index_dict = {}
member_list = []
last_member_id = 0


def add_member(name):
    global last_member_id
    last_member_index = last_member_id
    member_index_dict[name] = last_member_index

    new_member_id = last_member_id + 1
    new_member = {}
    new_member["name"] = name
    new_member["id"] = new_member_id
    new_member["grade"] = 0
    new_member["points"] = 0
    new_member["attend_num_wednesday"] = 0
    new_member["attend_num_weekend"] = 0
    member_list.append(new_member)

    last_member_id  = new_member_id


def get_member(name):
    if name not in member_index_dict:
        add_member(name)

    return member_list[member_index_dict[name]]


def check_attendance(name, attendance_day):
    member = get_member(name)

    add_attendance_points(attendance_day, member)


def add_attendance_points(attendance_day, member):
    add_point = 0
    index = 0
    if attendance_day == "monday":
        index = 0
        add_point += 1
    elif attendance_day == "tuesday":
        index = 1
        add_point += 1
    elif attendance_day == "wednesday":
        index = 2
        add_point += 3
        member["attend_num_wednesday"] += 1
    elif attendance_day == "thursday":
        index = 3
        add_point += 1
    elif attendance_day == "friday":
        index = 4
        add_point += 1
    elif attendance_day == "saturday":
        index = 5
        add_point += 2
        member["attend_num_weekend"] += 1
    elif attendance_day == "sunday":
        index = 6
        add_point += 2
        member["attend_num_weekend"] += 1
    member["points"] += add_point


def check_bonus_points():
    for member in member_list:
        if member["attend_num_wednesday"] > 9:
            member["points"] += 10
        if member["attend_num_weekend"] > 9:
            member["points"] += 10


def get_grade():
    for member in member_list:
        if member["points"] >= 50:
            member["grade"] = "GOLD"
        elif member["points"] >= 30:
            member["grade"] = "SILVER"
        else:
            member["grade"] = "NORMAL"

        print(f"NAME : {member["name"]}, POINT : {member["points"]}, GRADE : {member["grade"]}")


def remove_player():
    print("\nRemoved player")
    print("==============")
    for member in member_list:
        if member["grade"] in ("GOLD", "SILVER"):
            continue
        if member["attend_num_wednesday"] != 0:
            continue
        if member["attend_num_weekend"] != 0:
            continue
        print(member["name"])


def input_attendance_data(read_data):
    for data in read_data:
        parts = data.strip().split()
        if len(parts) != 2:
            continue

        check_attendance(name=parts[0], attendance_day=parts[1])


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

        check_bonus_points()

        get_grade()

        remove_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
