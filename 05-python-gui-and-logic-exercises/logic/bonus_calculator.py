"""Bonus tiers from performance and attendance.

p >= 90 and a >= 95 -> 20%   |   p >= 80 and a >= 90 -> 10%
p >= 70             -> 5%    |   otherwise            -> no bonus
"""


def bonus():
    performance = int(input("what's your performance "))
    attendance = int(input("what's your attendance "))
    if performance < 1 or attendance < 1:
        raise ValueError("enter a valid number")

    if performance >= 90 and attendance >= 95:
        print("your bonus is 20%")
    elif performance >= 80 and attendance >= 90:
        print("your bonus is 10%")
    elif performance >= 70:
        print("your bonus is 5%")
    else:
        print("no bonus")


if __name__ == "__main__":
    bonus()
