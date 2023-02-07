from collections import Counter

def counting_duplicates(text: str) -> int:
    return len([key for key, value in Counter(text.lower()).items() if value > 1])


print(counting_duplicates("abcde"))# == 0 # символи не повторюються більше одного разу
print(counting_duplicates("aabbcde"))# == 2 # 'a' і 'b'
# print(counting_duplicates("aabBcde"))# == 2 # 'a' зустрічається двічі, 'b' зустрічається двічі (`b` і `B`)
# print(counting_duplicates("indivisibility"))# == 1 # "i" зустрічається шість разів
# print(counting_duplicates("Indivisibilities"))# == 2 # "i" зустрічається сім разів, а "s" зустрічається двічі
# print(counting_duplicates("aA11"))# == 2 # 'a' і '1'
# print(counting_duplicates("ABBA"))# == 2 # "A" і "B" зустрічаються двічі
