import sys


def calc_sum(a, b):
    """Takes two numbers and returns their sum"""
    return a + b


def cycle_sum(numbers):
    """Takes a list of numbers and cycles through them returning the sum of each pair of numbers"""
    total = 0
    for i in range(len(numbers)):
        total += calc_sum(numbers[i], numbers[(i + 1) % len(numbers)])
    return total


if __name__ == "__main__":
    cycle_sum(sys.argv[1])
