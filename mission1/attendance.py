member_dict = {}
member_list = []
last_member_id = 0

# dat[사용자ID][요일]
dat = [[0] * 100 for _ in range(100)]
grade = [0] * 100
attend_num_wednesday = [0] * 100
attend_num_weekend = [0] * 100

def add_member(name):
    global last_member_id
    last_member_id += 1
    new_member = {}
    member_dict[name] = last_member_id
    new_member["name"] = name
    new_member["id"] = last_member_id
    new_member["grade"] = 0
    new_member["points"] = 0
    new_member["attend_wednesday"] = 0
    new_member["attend_weekend"] = 0
    member_list.append(new_member)


def get_member_id(name):
    if name not in member_dict:
        add_member(name)

    return member_dict[name]


def check_attendance(name, attendance_day):
    member_id = get_member_id(name)

    add_attendance_points(attendance_day, member_id)


def add_attendance_points(attendance_day, member_id):
    add_point = 0
    index = 0
    member_list_index = member_id - 1
    if attendance_day == "monday":
        index = 0
        add_point += 1
    elif attendance_day == "tuesday":
        index = 1
        add_point += 1
    elif attendance_day == "wednesday":
        index = 2
        add_point += 3
        attend_num_wednesday[member_id] += 1
    elif attendance_day == "thursday":
        index = 3
        add_point += 1
    elif attendance_day == "friday":
        index = 4
        add_point += 1
    elif attendance_day == "saturday":
        index = 5
        add_point += 2
        attend_num_weekend[member_id] += 1
    elif attendance_day == "sunday":
        index = 6
        add_point += 2
        attend_num_weekend[member_id] += 1
    dat[member_id][index] += 1
    member_list[member_list_index]["points"] += add_point


def check_bonus_points(member_id):
    member_list_index = member_id - 1
    if dat[member_id][2] > 9:
        member_list[member_list_index]["points"] += 10
    if dat[member_id][5] + dat[member_id][6] > 9:
        member_list[member_list_index]["points"] += 10


def get_grade(member_id):
    member_list_index = member_id - 1
    if member_list[member_list_index]["points"] >= 50:
        grade[member_id] = 1
    elif member_list[member_list_index]["points"] >= 30:
        grade[member_id] = 2
    else:
        grade[member_id] = 0

    print(f"NAME : {member_list[member_list_index]["name"]}, POINT : {member_list[member_list_index]["points"]}, GRADE : ", end="")

    if grade[member_id] == 1:
        print("GOLD")
    elif grade[member_id] == 2:
        print("SILVER")
    else:
        print("NORMAL")


def remove_player():
    print("\nRemoved player")
    print("==============")
    for member_id in range(1, last_member_id + 1):
        if grade[member_id] in (1, 2):
            continue
        if attend_num_wednesday[member_id] != 0:
            continue
        if attend_num_weekend[member_id] != 0:
            continue
        member_list_index = member_id - 1
        print(member_list[member_list_index]["name"])


def open_input_file():
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        for _ in range(500):
            line = f.readline()
            if not line:
                break
            parts = line.strip().split()
            if len(parts) != 2:
                break
            check_attendance(name=parts[0], attendance_day=parts[1])


def main():
    try:
        open_input_file()

        for member_id in range(1, last_member_id + 1):
            check_bonus_points(member_id)

            get_grade(member_id)

        remove_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
