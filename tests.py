
from dicelib import dicelib


# This is a good test with Nose. (For reference)
def test_Coin():
    coin = dicelib.Coin()
    if 1 <= coin.roll() <= 2:
        assert True
    else:
        assert False


def test_DFour():
    dFour = dicelib.DFour()
    yield check_dice, dFour


def test_DSix():
    dSix = dicelib.DSix()
    yield check_dice, dSix


def test_DEight():
    dEight = dicelib.DEight()
    yield check_dice, dEight


def test_DTen():
    dTen = dicelib.DTen()
    yield check_dice, dTen


def test_DPercentile():
    dPercent = dicelib.DPercentile()
    yield check_percentile, dPercent


def test_DTwelve():
    dTwelve = dicelib.DTwelve()
    yield check_dice, dTwelve


def test_DTwenty():
    dTwenty = dicelib.DTwenty()
    yield check_dice, dTwenty


def DOneHundred():
    dOneHundred = dicelib.DOneHundred()
    yield check_dice, dOneHundred


def check_dice(die):
    if 1 <= die.roll() <= die.sides:
        assert True
    else:
        assert False


def check_percentile(die):
    if 1 <= die.roll() <= die.tensDice.sides * 10:
        assert True
    else:
        assert False
