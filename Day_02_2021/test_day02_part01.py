import pytest
import os

from part01 import calculate_submarine_position

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Specify the full path to 'input.txt'
input_file_path = os.path.join(script_dir, 'input.txt')

@pytest.fixture
def real_input():
  with open('input.txt', 'r') as f:
    commands = [line.strip() for line in f]

  return commands

@pytest.fixture
def example_input():
  return [
      'forward 2',
      'down 9',
      'up 6',
      'forward 1',
      'down 5',
      'down 7',
  ]



def test_calculate_submarine_position_example_input(example_input):
  expected_position = (3, 15)

  actual_position = calculate_submarine_position(example_input)

  assert actual_position == expected_position


def test_calculate_submarine_position_real_input(real_input):
  expected_position = (2010, 1030)

  actual_position = calculate_submarine_position(real_input)

  assert actual_position == expected_position