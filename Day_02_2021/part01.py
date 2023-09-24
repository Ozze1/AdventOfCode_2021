def calculate_submarine_position(commands):
  """Calculates the final horizontal position and depth of a submarine after following a series of commands.

  Args:
    commands: A list of commands.

  Returns:
    A tuple containing the final horizontal position and depth of the submarine.
  """

  horizontal_position = 0
  depth = 0

  for command in commands:
    direction, magnitude = command.split(' ')

    if direction == 'forward':
      horizontal_position += int(magnitude)
    elif direction == 'down':
      depth += int(magnitude)
    elif direction == 'up':
      depth -= int(magnitude)

  return horizontal_position, depth


def main():
  with open('input.txt', 'r') as f:
    commands = [line.strip() for line in f]

  horizontal_position, depth = calculate_submarine_position(commands)

  answer = horizontal_position * depth

  print(answer)


if __name__ == '__main__':
  main()