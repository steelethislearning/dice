from distutils.core import setup

# Package installation for Dice Library'

files = ["dicelib/*"]

setup(name="DiceLib",
      version='1.0',
      description="Library of Common Dice Types",
      author="Josh Steele",
      author_email="josh@steelethis.com",
      url="https://github.com/steelethislearning/dice",
      packages=['dicelib'],
      long_description="""
        This library contains some common dice types, as well as a Coin class.
        It should be useful for any dice that need to be included into any
        existing code.
      """
      )
