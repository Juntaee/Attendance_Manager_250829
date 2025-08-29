import pytest
from pytest_mock import MockerFixture
from mission2.grade_factory import GradeFactory
from mission2.grades import Grade, Gold, Silver, Normal


def test_factory_instance_grade_case(mocker: MockerFixture):
    grade_factory = GradeFactory()

    grade = grade_factory.determine_grade(90)

    assert isinstance(grade, Grade)


def test_factory_instance_gold_case(mocker: MockerFixture):
    grade_factory = GradeFactory()

    grade = grade_factory.determine_grade(90)

    assert grade.get_name() == "GOLD"


def test_factory_instance_silver_case(mocker: MockerFixture):
    grade_factory = GradeFactory()

    grade = grade_factory.determine_grade(40)

    assert grade.get_name() == "SILVER"


def test_factory_instance_normal_case(mocker: MockerFixture):
    grade_factory = GradeFactory()

    grade = grade_factory.determine_grade(20)

    assert grade.get_name() == "NORMAL"