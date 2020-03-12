def is_sorted(li, index):
    if index == (len(li)-1):

        return True
    current = li[index] <= li[index + 1]
    remaining = is_sorted(li, index+1)
    return current and remaining

def contains(li, target, index=0):

    if index == len(li):
        return False
    current = li[inedx] ==target
    remaining = contains(li, target, index +1)

    return current and remaining
print(contains([45,56,77], 55))
