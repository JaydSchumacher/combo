# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]


def combo(*args):
    my_list = []
    count = 0
    item_len = 0
    for item in args:
        item_len = len(item)
    for x in range(item_len):
        my_tup = (args[0][count], args[1][count])
        my_list.append(my_tup)
        count += 1
    return my_list

print(combo([1, 2, 3], 'abc'))