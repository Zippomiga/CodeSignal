# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)", the output should be
# solution(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# solution(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# solution(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# solution(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".


def solution(inputString):
    S = inputString
    
    while "(" in S:
        op = S.rfind("(")
        cl = S.find(")", op)

        rep = S[op:cl +1]
        inv = S[op +1:cl][::-1]

        S = S.replace(rep, inv)

    return S

# <--------------- Others --------------->

def solution(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s