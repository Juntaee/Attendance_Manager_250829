from unittest.mock import mock_open
import pytest
from pytest_mock import MockerFixture

from mission2.attendance_manager import AttendanceManager

def test_file_open_called(capsys: pytest.CaptureFixture, mocker: MockerFixture):
    mock_open_file = mocker.patch('builtins.open', mock_open(read_data=''))
    attendance_manager = AttendanceManager()

    attendance_manager.manage_attendance()

    assert mock_open_file.called


def test_output_success_message(capsys: pytest.CaptureFixture, mocker: MockerFixture):
    FILE_PATH = "../attendance_weekday_500.txt"
    mocker.patch('mission2.attendance_manager.AttendanceManager.get_file_path', return_value=FILE_PATH)
    attendance_manager = AttendanceManager()

    attendance_manager.manage_attendance()
    captured = capsys.readouterr()
    ouput = captured.out

    assert ('NAME : Umar, POINT : 48, GRADE : SILVER\n'
             'NAME : Daisy, POINT : 45, GRADE : SILVER\n'
             'NAME : Alice, POINT : 61, GRADE : GOLD\n'
             'NAME : Xena, POINT : 91, GRADE : GOLD\n'
             'NAME : Ian, POINT : 23, GRADE : NORMAL\n'
             'NAME : Hannah, POINT : 127, GRADE : GOLD\n'
             'NAME : Ethan, POINT : 44, GRADE : SILVER\n'
             'NAME : Vera, POINT : 22, GRADE : NORMAL\n'
             'NAME : Rachel, POINT : 54, GRADE : GOLD\n'
             'NAME : Charlie, POINT : 58, GRADE : GOLD\n'
             'NAME : Steve, POINT : 38, GRADE : SILVER\n'
             'NAME : Nina, POINT : 79, GRADE : GOLD\n'
             'NAME : Bob, POINT : 8, GRADE : NORMAL\n'
             'NAME : George, POINT : 42, GRADE : SILVER\n'
             'NAME : Quinn, POINT : 6, GRADE : NORMAL\n'
             'NAME : Tina, POINT : 24, GRADE : NORMAL\n'
             'NAME : Will, POINT : 36, GRADE : SILVER\n'
             'NAME : Oscar, POINT : 13, GRADE : NORMAL\n'
             'NAME : Zane, POINT : 1, GRADE : NORMAL\n'
             '\n'
             'Removed player\n'
             '==============\n'
             'Bob\n'
             'Zane\n') == ouput


def test_file_read_error_message(capsys: pytest.CaptureFixture, mocker: MockerFixture):
    FILE_PATH = "../attendance_weekday_50001.txt"
    mocker.patch('mission2.attendance_manager.AttendanceManager.get_file_path', return_value=FILE_PATH)
    attendance_manager = AttendanceManager()

    attendance_manager.manage_attendance()
    captured = capsys.readouterr()
    ouput = captured.out

    assert '파일을 찾을 수 없습니다.' in ouput