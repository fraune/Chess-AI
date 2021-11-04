from enum import Enum


def test_duck_creator():
    md1 = create_duck(DuckType.MALLARD)
    md2 = create_duck(DuckType.MALLARD)
    assert md1.my_sound == 'quack'
    assert md2.my_sound == 'quack'
    md1.my_sound = 'hi'
    assert md1.my_sound == 'hi'
    assert md2.my_sound == 'quack'


class DuckType(Enum):
    MALLARD = 1
    RUBBER = 2


def create_duck(type: DuckType):
    if type is DuckType.MALLARD:
        return MallardDuck()
    elif type is DuckType.RUBBER:
        return RubberDuck()
    else:
        raise ValueError(f'Unknown DuckType: {type}')


class Duck:
    my_sound: str

    def __init__(self):
        self.my_sound = "unknown"


class MallardDuck(Duck):
    def __init__(self):
        self.my_sound = 'quack'


class RubberDuck(Duck):
    def __init__(self):
        self.my_sound = 'squeak'
