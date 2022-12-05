# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# solution(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]


def solution(picture):
    ast = '*' * (len(picture[0]) +2)
    bdr = [ast, ast]
    
    for i in range(len(picture)):
        bdrStr = '*' + picture[i] + '*'
        bdr.insert(i +1, bdrStr)

    return bdr