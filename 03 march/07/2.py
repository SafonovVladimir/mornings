def student_att(records: str) -> bool:
    return records.count("A") < 2 and "LLL" not in records

print(student_att("PPPPP"))# is True
print(student_att("APLL"))# is True
print(student_att("LLLL"))# is False
print(student_att("APPPPPA"))# is False
