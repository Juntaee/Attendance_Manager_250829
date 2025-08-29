from typing_extensions import override
from grade_base import Grade

class Gold(Grade):
    def __init__(self):
        self.name = 'GOLD'

    @override
    def determine(self, point: int) -> bool:
        if point >= 50:
            return True
        return False

    @override
    def get_name(self) -> str:
        return self.name


class Silver(Grade):
    def __init__(self):
        self.name = 'SILVER'

    @override
    def determine(self, point: int) -> bool:
        if 30 <= point < 50:
            return True
        return False

    @override
    def get_name(self) -> str:
        return self.name


class Normal(Grade):
    def __init__(self):
        self.name = 'NORMAL'

    @override
    def determine(self, point: int) -> bool:
        if point < 30:
            return True
        return False

    @override
    def get_name(self) -> str:
        return self.name