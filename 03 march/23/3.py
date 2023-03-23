def negation_value(negations: str, val: bool) -> bool:
    return not bool(val) if negations.count("!") % 2 else bool(val)


print(negation_value("!", False)) # повертає True
print(negation_value("!!!!!", True)) # повертає False
print(negation_value("!!", [])) # повертає False
print(negation_value("", False))  # повертає False
