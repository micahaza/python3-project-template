from random import randint


def random_damage(modifier):
    roll = randint(1, 8)
    return modifier + roll
