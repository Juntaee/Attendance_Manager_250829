# Global value
MAX_FILE_LINE = 500
MAX_USER_NUMBER = 100

points = [0] * MAX_USER_NUMBER
grade = [0] * MAX_USER_NUMBER
user_name_list = [''] * MAX_USER_NUMBER
training_day_cnt = [0] * MAX_USER_NUMBER
weekend_cnt = [0] * MAX_USER_NUMBER
total_uniform_number = 0
user_number_dict = {}

attendance_file = "attendance_weekday_500.txt"
UTF_8 = 'utf-8'

# Days info
MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"
SATURDAY = "saturday"
SUNDAY = "sunday"

days_dict = {MONDAY: 0, TUESDAY: 1, WEDNESDAY: 2, THURSDAY: 3, FRIDAY: 4, SATURDAY: 5, SUNDAY: 6}
all_day = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]
weekend_day = [SATURDAY, SUNDAY]
training_day = [WEDNESDAY]

# Grade classification
GOLD = 1
SILVER = 2
NORMAL = 0


def calc_basic_points(user_name, day_of_week):
    register_uniform_number(user_name)
    user_number = user_number_dict[user_name]

    if day_of_week not in all_day:
        raise ValueError

    if day_of_week in training_day:
        points[user_number] += 3
        training_day_cnt[user_number] += 1
    elif day_of_week in weekend_day:
        points[user_number] += 2
        weekend_cnt[user_number] += 1
    else:
        points[user_number] += 1


def register_uniform_number(user_name):
    global total_uniform_number
    if user_name not in user_number_dict:
        total_uniform_number += 1
        user_number_dict[user_name] = total_uniform_number
        user_name_list[total_uniform_number] = user_name


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for user_num in range(1, total_uniform_number + 1):
        if grade[user_num] not in (GOLD, SILVER) and training_day_cnt[user_num] == 0 and \
                weekend_cnt[user_num] == 0:
            print(user_name_list[user_num])


def print_gold_silver_player():
    for user_num in range(1, total_uniform_number + 1):
        print(f"NAME : {user_name_list[user_num]}, POINT : {points[user_num]}, GRADE : ", end="")
        if grade[user_num] == GOLD:
            print("GOLD")
        elif grade[user_num] == SILVER:
            print("SILVER")
        else:
            print("NORMAL")


def classify_grade():
    for user_num in range(1, total_uniform_number + 1):
        if points[user_num] >= 50:
            grade[user_num] = GOLD
        elif points[user_num] >= 30:
            grade[user_num] = SILVER
        else:
            grade[user_num] = NORMAL


def calc_bonus_points():
    for user_num in range(1, total_uniform_number + 1):
        if training_day_cnt[user_num] > 9:
            points[user_num] += 10
        if weekend_cnt[user_num] > 9:
            points[user_num] += 10


def parse_file_info():
    try:
        with open(attendance_file, encoding=UTF_8) as f:
            for _ in range(MAX_FILE_LINE):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) != 2:
                    raise ValueError
                calc_basic_points(parts[0], parts[1])
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def manage_attendance():
    parse_file_info()
    calc_bonus_points()
    classify_grade()
    print_gold_silver_player()
    print_removed_player()


if __name__ == "__main__":
    manage_attendance()
