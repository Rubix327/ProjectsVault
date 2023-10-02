def get_h_index(lst):
    lst.sort()

    lng = len(lst)
    for pi in range(lng):
        if lst[pi] >= lng - pi:
            return lng - pi
    return 0


print(get_h_index([100]))
print(get_h_index([3, 0, 6, 1, 5]))
print(get_h_index([1, 3, 1]))

