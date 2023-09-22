def count_depth_increases(input_file):

  depth_measurements = []
  for line in input_file:
    depth_measurements.append(int(line))

  count = 0
  for i in range(1, len(depth_measurements)):
    if depth_measurements[i] > depth_measurements[i - 1]:
      count += 1

  return count


def test_count_depth_increases():
  
  depth_measurements = [1, 2]
  count = count_depth_increases(depth_measurements)
  assert count == 1

if __name__ == '__main__':
  test_count_depth_increases()