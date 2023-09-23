def count_depth_increases_sliding_window(depth_measurements):
  """Counts the number of times the sum of a three-measurement sliding window increases from one measurement to the next.

  Args:
    depth_measurements: A list of depth measurements.

  Returns:
    The number of times the sum of a three-measurement sliding window increases from one measurement to the next.
  """

  sums = []
  for i in range(len(depth_measurements) - 2):
    sum = depth_measurements[i] + depth_measurements[i + 1] + depth_measurements[i + 2]
    sums.append(sum)

  count = 0
  for i in range(1, len(sums)):
    if sums[i] > sums[i - 1]:
      count += 1

  return count


if __name__ == '__main__':
  with open('input.txt', 'r') as f:
    depth_measurements = [int(line) for line in f]

  count = count_depth_increases_sliding_window(depth_measurements)

  print(count)