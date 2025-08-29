from grade_factory import GradeFactory
from user import User

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

FILE_PATH = "attendance_weekday_500.txt"
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
GOLD = "GOLD"
SILVER = "SILVER"
NORMAL = "NORMAL"

class AttendanceManager:
    def __init__(self):
        self.user_list: list[User] = []
        self.grade_factory: GradeFactory = GradeFactory()


    def create_user_instance(self, user_name: str, user_num: int, point: int, grade_factory: GradeFactory) -> User:
        return User(name=user_name, number=user_num, point=point, grade_factory=grade_factory)


    def make_user_list(self):
        for user_num in range(1, total_uniform_number + 1):
            user = self.create_user_instance(user_name_list[user_num], user_num, points[user_num], self.grade_factory)
            self.user_list.append(user)


    def calc_basic_points(self, user_name, day_of_week):
        self.register_uniform_number(user_name)
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


    def register_uniform_number(self, user_name):
        global total_uniform_number
        if user_name not in user_number_dict:
            total_uniform_number += 1
            user_number_dict[user_name] = total_uniform_number
            user_name_list[total_uniform_number] = user_name


    def print_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for user in self.user_list:
            if user.get_grade() not in (GOLD, SILVER) and training_day_cnt[user.get_number()] == 0 and \
                    weekend_cnt[user.get_number()] == 0:
                print(user.get_name())


    def print_gold_silver_player(self):
        for user in self.user_list:
            print(f"NAME : {user.get_name()}, POINT : {user.get_point()}, GRADE : {user.get_grade()}")


    def classify_grade(self):
        for user in self.user_list:
            user.compute_grade()


    def calc_bonus_points(self):
        for user_num in range(1, total_uniform_number + 1):
            if training_day_cnt[user_num] > 9:
                points[user_num] += 10
            if weekend_cnt[user_num] > 9:
                points[user_num] += 10


    def get_file_path(self):
        return FILE_PATH


    def parse_file_info(self):
        try:
            with open(self.get_file_path(), encoding=UTF_8) as f:
                for _ in range(MAX_FILE_LINE):
                    line = f.readline()
                    if not line:
                        break
                    parts = line.strip().split()
                    if len(parts) != 2:
                        raise ValueError
                    self.calc_basic_points(parts[0], parts[1])
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")


    def manage_attendance(self):
        self.parse_file_info()
        self.calc_bonus_points()
        self.make_user_list()
        self.classify_grade()
        self.print_gold_silver_player()
        self.print_removed_player()


if __name__ == "__main__":
    AttendanceManager().manage_attendance()
