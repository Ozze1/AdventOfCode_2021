def count_depth_increases(input_file):
  """Counts the number of times the depth measurement increases from one line to the next in the input file.

  Args:
    input_file: A file object containing the input data.

  Returns:
    The number of times the depth measurement increases from one line to the next.
  """

  depth_measurements = []
  for line in input_file:
    depth_measurements.append(int(line))

  count = 0
  for i in range(1, len(depth_measurements)):
    if depth_measurements[i] > depth_measurements[i - 1]:
      count += 1

  return count


if __name__ == '__main__':
  with open('input.txt', 'r') as f:
    count = count_depth_increases(f)

  print(count)