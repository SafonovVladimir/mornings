from abc import ABC


class Human(ABC):
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def god() -> list:
    return [Man(), Woman()]
