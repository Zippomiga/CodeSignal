# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".


def solution(s1, s2):
    def ab(e): return len(e)
    asc = [s1, s2]
    asc.sort(key=ab)
    sMin, sMax, C = list(asc[0]), list(asc[1]), 0

    for x in sMin:
        if x in sMax:
            sMax.remove(x)
            C += 1

    return C


# <--------------- Others --------------->

def solution(s1, s2):
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))