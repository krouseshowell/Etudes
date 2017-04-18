#See permutations.py for my attempt to do this without shortcuts
def permutations(str):
    lst = []
    from itertools import permutations
    letters = list(str)
    perm = permutations(letters)
    for i in list(perm):
        lst.append(("").join(i))
    lst = set(lst)
    return list(lst)



print permutations("abc")
