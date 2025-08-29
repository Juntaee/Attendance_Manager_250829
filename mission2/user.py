from grade_factory import Grade, GradeFactory

class User:
    def __init__(self, name: str, number: int, point: int, grade_factory: GradeFactory):
        self._name = name
        self._number = number
        self._point = point
        self._grade_factory = grade_factory
        self._grade : Grade = None

    def get_name(self) -> str:
        return self._name

    def get_number(self) -> int:
        return self._number

    def get_point(self) -> int:
        return self._point

    def get_grade(self) -> str:
        return self._grade.get_name()

    def compute_grade(self):
        self._grade = self._grade_factory.determine_grade(self._point)