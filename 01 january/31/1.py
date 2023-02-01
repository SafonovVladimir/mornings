def credit_card_mask(card_number: str) -> str:
    if len(card_number) <= 4:
        return card_number
    else:
        return "#" * (len(card_number) - 4) + card_number[-4:]

print(credit_card_mask("4556364607935616"))
print(credit_card_mask("64607935616"))
print(credit_card_mask("55556"))
print(credit_card_mask("1"))
print(credit_card_mask(""))
