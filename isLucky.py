# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# solution(n) = true;
# For n = 239017, the output should be
# solution(n) = false.


def solution(n):
    s = str(n)
    l = len(s) // 2
    mid1, mid2 = s[:l], s[l:]

    half1 = sum([int(x) for x in mid1])
    half2 = sum([int(x) for x in mid2])

    return half1 == half2

# <--------------- Others --------------->

def solution(n):
    n = list(map(int, str(n)))
    l = len(n) // 2
    return sum(n[:l]) == sum(n[l:])