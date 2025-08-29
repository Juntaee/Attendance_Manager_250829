import pytest
from pytest_mock import MockerFixture
from mission2.grades import Gold, Silver, Normal

def test_gold_name_success(mocker: MockerFixture):
    gold = Gold()

    assert gold.get_name() == "GOLD"


def test_silver_name_success(mocker: MockerFixture):
    silver = Silver()

    assert silver.get_name() == "SILVER"


def test_normal_name_success(mocker: MockerFixture):
    normal = Normal()

    assert normal.get_name() == "NORMAL"

def test_gold_determine_success(mocker: MockerFixture):
    gold = Gold()

    assert gold.determine(60) == True


def test_silver_determine_success(mocker: MockerFixture):
    silver = Silver()

    assert silver.determine(40) == True


def test_normal_determine_success(mocker: MockerFixture):
    normal = Normal()

    assert normal.determine(20) == True
