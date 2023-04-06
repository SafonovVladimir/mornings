def palindromic_substring(string: str) -> str:
    if len(string) <= 1 or string == string[::-1]:
        return string

    start, max_len = 0, 1

    for i in range(1, len(string)):
        odd = string[i - max_len - 1:i + 1]
        even = string[i - max_len:i + 1]

        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue

        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1

        print(odd)
        print(even)

    return string[start:start + max_len]


print(palindromic_substring("babad"))
# print(palindromic_substring("cbbd"))
# print(palindromic_substring(
#     "bljv1a23iiwe44bv8fcdjsfdjs238dbsda23sd48fds3assdaagdha434sd32432sd423423ewhehwie2d34fd824hidhkdsfkjd"
# ))
