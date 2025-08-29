import pytest
from pytest_mock import MockerFixture
from mission2.user import User

def test_name_success_case(mocker: MockerFixture):
    mock_factory = mocker.Mock()
    user = User(name="Sally", number=1, point=38, grade_factory=mock_factory)

    assert user.get_name() == "Sally"

def test_number_success_case(mocker: MockerFixture):
    mock_factory = mocker.Mock()
    user = User(name="Sally", number=1, point=38, grade_factory=mock_factory)

    assert user.get_number() == 1

def test_point_success_case(mocker: MockerFixture):
    mock_factory = mocker.Mock()
    user = User(name="Sally", number=1, point=38, grade_factory=mock_factory)

    assert user.get_point() == 38