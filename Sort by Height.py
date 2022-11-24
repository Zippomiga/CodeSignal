# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


def solution(a):
    tree = -1
    heights = sorted([x for x in a if x != tree])

    for i in range(len(a)):
        if a[i] == tree: heights.insert(i, tree)

    return heights

# <--------------- Others --------------->

def solution(a):
    people = sorted(filter(lambda x: x != -1, a))
    return [people.pop(0) if i != -1 else -1 for i in a]