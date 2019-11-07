"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if dice.count(dice[0]) == len(dice) else 0
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: dice.count(2) * 2
THREES = lambda dice: dice.count(3) * 3
FOURS = lambda dice: dice.count(4) * 4
FIVES = lambda dice: dice.count(5) * 5
SIXES = lambda dice: dice.count(6) * 6
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and 1 < dice.count(dice[0]) < 4 else 0
FOUR_OF_A_KIND = lambda dice: sorted(dice)[1] * 4 if dice.count(sorted(dice)[1]) >= 4 else 0
LITTLE_STRAIGHT = lambda dice: 30 if len(set(dice)) == 5 and max(dice) == 5 else 0
BIG_STRAIGHT = lambda dice: 30 if len(set(dice)) == 5 and min(dice) == 2 else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)
