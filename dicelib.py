# Dice Library
# Contains various dice and what you can do with them.

from random import randint


class Die:
    """
    Base class that all dice come from.
    Can be used to create custom dice as well.
    """

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


class Coin(Die):
    """
    A 2 sided die.  Technically not a die,
    but with a coin you can roll a 1 or 2, or heads or tails respectively.
    """

    def __init__(self):
        self.sides = 2


class DFour(Die):

    def __init__(self):
        self.sides = 4


class DSix(Die):

    def __init__(self):
        self.sides = 6


class DEight(Die):

    def __init__(self):
        self.sides = 8


class DTen(Die):

    def __init__(self):
        self.sides = 10


class DPercentile(Die):
    """
    Dice that rolls a percentage value.
    Consists of a standard D10 and another D10 with Tens on each side.
    """

    def __init__(self):
        self.onesDice = DTen()
        self.tensDice = DTen()

    def roll(self):
        ones = self.onesDice.roll() - 1
        tens = self.tensDice.roll() * 10
        rollValue = tens + ones
        return rollValue


class DTwelve(Die):

    def __init__(self):
        self.sides = 12


class DTwenty(Die):

    def __init__(self):
        self.sides = 20


class DOneHundred(Die):

    def __init__(self):
        self.sides = 100
