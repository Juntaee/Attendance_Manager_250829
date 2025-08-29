from grades import Grade, Gold, Silver, Normal

class GradeFactory:
    def __init__(self):
        # singleton pattern
        self.grades = [Gold(), Silver(), Normal()]

    # factory pattern
    def determine_grade(self, point: int) -> Grade:
        for grade in self.grades:
            if grade.determine(point):
                return grade