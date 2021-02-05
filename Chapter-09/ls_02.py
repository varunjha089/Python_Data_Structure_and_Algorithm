def search(lists, term):
    for i in range(len(lists)):
        if term == lists[i]:
            return i
        elif lists[i] > term:
            return None
    return None