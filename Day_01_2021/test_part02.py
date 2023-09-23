import pytest

from cachetools import cached, LRUCache

cache = LRUCache(maxsize=100)

@cached(cache=cache)
def load_input_file():
  with open('input.txt', 'r') as f:
    depth_measurements = [int(line) for line in f]
    return depth_measurements


def count_depth_increases_sliding_window(depth_measurements):

  sums = []
  for i in range(len(depth_measurements) - 2):
    sum = depth_measurements[i] + depth_measurements[i + 1] + depth_measurements[i + 2]
    sums.append(sum)

  count = 0
  for i in range(1, len(sums)):
    if sums[i] > sums[i - 1]:
      count += 1

  return count


@pytest.fixture
def example_input():
  return [3]


@pytest.fixture
def real_input():
  return load_input_file()


def test_example_input(example_input):
  expected_count = 0

  actual_count = count_depth_increases_sliding_window(example_input)

  assert expected_count == actual_count


def test_real_input(real_input):
  expected_count = 1523

  actual_count = count_depth_increases_sliding_window(real_input)

  assert expected_count == actual_count