class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        reverse_letter_list = []

        for char in s:
            if char.lower().isalpha():
                reverse_letter_list.append(char)
        reverse_letter_list.reverse()

        for i in range(len(s)):
            if not s[i].isalpha():
                reverse_letter_list.insert(i, s[i])

        return "".join(reverse_letter_list)


# s = "Test1ng-Leet=code-Q!"
# s = "ab-cd" # "dc-ba"
s = "a-bC-dEf-ghIj" # "j-Ih-gfE-dCba"
string = Solution()
print(string.reverseOnlyLetters(s))

