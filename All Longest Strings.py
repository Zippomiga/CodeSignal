# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# solution(inputArray) = ["aba", "vcd", "aba"].

def solution(inputArray):
    maxStr = max([len(x) for x in inputArray])

    return [x for x in inputArray if (len(x) == maxStr)]

print(solution(["aba", "aa", "ad", "vcd", "aba"]))
print(solution(["abacaba", "abacab", "abac", "xxxxxx"]))
print(solution(["enyky", "benyky", "yely", "varennyky"]))