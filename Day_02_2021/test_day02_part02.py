import pytest
import os

from part02 import calculate_submarine_position_with_aim

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Specify the full path to 'input.txt'
input_file_path = os.path.join(script_dir, 'input.txt')

@pytest.fixture
def real_input():
  with open(input_file_path, 'r') as f:
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

def test_calculate_submarine_position_with_aim_example_input(example_input):
  expected_position = (3)

  actual_position, actual_aim = calculate_submarine_position_with_aim(example_input)

  assert actual_position == expected_position
  assert actual_aim == 3


def test_calculate_submarine_position_with_aim_real_input(real_input):
  expected_position = (2010)

  actual_position, actual_aim = calculate_submarine_position_with_aim(real_input)

  assert actual_position == expected_position
  assert actual_aim == 1034321
