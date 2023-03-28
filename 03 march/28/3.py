def longest_substring(string: str) -> int:
    seen = set()
    start = longest_length = 0

    for end in range(len(string)):
        while string[end] in seen:
            seen.remove(string[start])
            start += 1
        seen.add(string[end])
        longest_length = max(longest_length, end - start + 1)

    return longest_length


# print(longest_substring(""))
# print(longest_substring("a"))
# print(longest_substring("12"))
print(longest_substring("skjdhaksjdhakjdhaskjdhasjkheiqwe928348344$#@RFDF$GGFHTYefafdwew4234tfgDFG3$3432432rseafDFASer233432e"))
print(longest_substring(" asdjgyeibmvo4328 57!@#$%^&*$ ")) #27