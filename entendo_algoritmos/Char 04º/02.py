def qsort(list_to_order: list[int]) -> list[int]:
    if len(list_to_order) < 2:
        return list_to_order

    #! The speed of this Algorithmn depends on it's pivot. Choose wiselly;

    pivot = list_to_order[0]
    less_than = [x for x in list_to_order[1:] if x < pivot]
    greater_than = [x for x in list_to_order[1:] if x >= pivot]

    return qsort(less_than) + [pivot] + qsort(greater_than)

l = [1, 50, 2]
l2 = [1, 50, 2, -3, 10 ,24, 100, 40, 32, 51, 66]
new = qsort(l[:])
print(new)
new2 = qsort(l2[:])
print(new2)
