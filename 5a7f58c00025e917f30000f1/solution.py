# Longest alphabetical substring
# https://www.codewars.com/kata/5a7f58c00025e917f30000f1

import string

ltr = string.ascii_lowercase


def longest(s):
    if len(s) < 2:
        return s

    result = s[0]
    stream = s[0]
    for i in range(1,len(s)):
        n = s[i]
        b = s[i-1]

        if ltr.index(n) >= ltr.index(b):
            stream += n
        else:
            stream = n

        if len(stream) > len(result):
            result = stream

    return result


print(longest('asd'), 'as')
print(longest('nab'), 'ab')
print(longest('abcdeapbcdef'), 'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
print(longest('asdfbyfgiklag'), 'fgikl')
print(longest('z'), 'z')
print(longest('zyba'), 'z')
