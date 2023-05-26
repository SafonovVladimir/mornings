# def solution(S):
#     result = []
#     last_occurrences = {}
#
#     for i in range(len(S) - 1):
#         digram = S[i:i+2]
#
#         if digram not in last_occurrences:
#             last_occurrences[digram] = [i]
#
#         else:
#             last_occurrences[digram].append(i)
#
#     for k, v in last_occurrences.items():
#         result.append(max(v) - min(v))
#
#     return max(result) if max(result) != 0 else -1
#
#
#
# # s = "aakmaakmakda"
# s = "aaa"
# # s = "codility"
# print(solution(s))

# lst = [1, 2, 3] * -1
# lst *= 2
# print(lst)
from collections import Counter

paragraph = ["The quick brown fox",
             "jumps over the lazy dog.",
             "The dog barks,",
             "and the fox runs away."
             ]


def word_frequency(paragraph: list) -> dict:
    return (dict(Counter(word.lower() for line in paragraph
                         for word in line.strip(".,").split())))


frequency = word_frequency(paragraph)
print(frequency)
