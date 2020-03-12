def eq_sum_list(unprocessed, first=(), second=()):


    if len(unprocessed) == 0:
        if sum(first) == sum(second):
            print(first, second)

        return
    item = unprocessed[0]
    eq_sum_list(unprocessed[1:], first + (item,), second)
    eq_sum_list(unprocessed[1:], first, second+(item,))

eq_sum_list((1,2,3))



