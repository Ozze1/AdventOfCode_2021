from part01 import calculate_submarine_position


def calculate_submarine_position_with_aim(commands):
  """Calculates the final horizontal position, depth, and aim of a submarine after following a series of commands.

  Args:
    commands: A list of commands.

  Returns:
    A tuple containing the final horizontal position, depth, and aim of the submarine.
  """

  horizontal_position = 0
  depth = 0
  aim = 0

  for command in commands:
    direction, magnitude = command.split(' ')

    if direction == 'forward':
      horizontal_position += int(magnitude)
      depth += aim * int(magnitude)
    elif direction == 'down':
      aim += int(magnitude)
    elif direction == 'up':
      aim -= int(magnitude)

  return horizontal_position, depth


def main():
  with open('input.txt', 'r') as f:
    commands = [line.strip() for line in f]

  horizontal_position, depth = calculate_submarine_position_with_aim(commands)

  answer = horizontal_position * depth

  print(answer)


if __name__ == '__main__':
  main()
