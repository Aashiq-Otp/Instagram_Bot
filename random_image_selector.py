import random


def should_like_or_not():
    num = (random.randrange(1, 100, 1)*random.randrange(4, 40, 1))
    choice = True
    if num % 2 != 0:
        choice = False
    return choice
