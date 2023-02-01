def credit_card_issuer_checking(number: int) -> str:
    str_number = str(number)
    if len(str_number) == 15 and str_number[:2] in ["34", "37"]:
        return "AMEX"
    if len(str_number) == 16 and str_number[:4] == "6011":
        return "Discover"
    if len(str_number) == 16 and str_number[:2] in ["51", "52", "53", "54", "55"]:
        return "Mastercard"
    if len(str_number) in [13, 16] and str_number[:1] == "4":
        return "VISA"
    else:
        return "Unknown"