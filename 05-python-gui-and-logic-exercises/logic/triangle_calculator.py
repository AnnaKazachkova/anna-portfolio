"""Right-triangle helper: angle and hypotenuse from height and base.

Demonstrates nested functions, default arguments and keyword-only arguments.
"""
import math


def main(height, base=8, *, name="Unknown room"):
    def my_angle(height, base):
        return math.atan(height / base) * 180 / math.pi

    def my_length(height, base):
        return math.sqrt(height ** 2 + base ** 2)

    return name, my_angle(height, base), my_length(height, base)


if __name__ == "__main__":
    print(main(height=10))
    print(main(height=10, base=12, name="Front Entrance"))
