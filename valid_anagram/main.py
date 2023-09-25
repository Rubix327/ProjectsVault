def is_anagram(first, second):
    lst = [c for c in first]

    for c in second:
        try:
            ind = lst.index(c)
            del lst[ind]
        except ValueError:
            return False

    return len(lst) == 0


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("лунь", "нуль"))
print(is_anagram("зов", "воз"))
