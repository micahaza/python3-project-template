import pytest
from myapp.damager import random_damage
from unittest import mock


input_data = [
    (dict(username='asasdf', email='bajgli+3@gmail.com', password='supersecret'), 200),
    (dict(username='goodusername', email='bajgli+4@gmail.com', password='asdfasdflong'), 200),
    (dict(username='badaboooo', email='bajgli+5@gmail.com', password='goodenough'), 200)
]


@pytest.mark.parametrize("test_input, expected_output", input_data)
def test_with_data(test_input, expected_output):
    assert test_input is not None
    assert 200 == expected_output


def test_a():
    assert True


@mock.patch("myapp.damager.randint", return_value=5, autospec=True)
def test_random_damage(mock_randint):
    assert random_damage(1) == 6
    mock_randint.assert_called_once_with(1, 8)
