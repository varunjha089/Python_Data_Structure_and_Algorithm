def search(lists, term):
    for i in range(len(lists)):
        if term == lists[i]:
            return i
    return 0
