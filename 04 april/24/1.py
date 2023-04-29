from collections import Counter
from itertools import groupby

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_counter = {}
        typed_counter = {}
        result = []

        for k, v in groupby(name):
            name_counter[k] = len(list(v))

        for k, v in groupby(typed):
            typed_counter[k] = len(list(v))

        print(name_counter)
        print(typed_counter)

        # for i in range(len(name_counter.items())):
        #     if list(name_counter)[i] != list(typed_counter)[i]:
        #         return False
        #
        #     if list(name_counter.values())[i] > list(typed_counter.values())[i]:
        #         result.append(False)
        #     else:
        #         result.append(True)
        #
        # return all(result)

name1 = "alex"
typed1 = "aaleexa"

name2 = "saeed"
typed2 = "ssaaedd"

name3 = "rick"
typed3 = "kric"

test = Solution()
print(test.isLongPressedName(name1, typed1))
print(test.isLongPressedName(name2, typed2))
print(test.isLongPressedName(name3, typed3))
