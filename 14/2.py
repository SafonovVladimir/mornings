def printer_errors(printer_label: str) -> str:
    forbidden_chars = ["n", "o", "p", "r", "s", "q", "t", "u", "v", "w", "x", "y", "z"]
    forbidden_count = 0
    for char in printer_label:
        if char in forbidden_chars:
            forbidden_count += 1
    result = str(f"{forbidden_count}/{len(printer_label)}")
    return result


print(printer_errors("abcdxyz"))# == "3/7" # 3 букви поза діапазоном та довжина рядка – 7

print(printer_errors("mmmm"))# == "0/4" # 0 букв поза діапазоном та довжина рядка – 4
