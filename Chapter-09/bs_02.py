def binary_search(lists, start, end, term):
    if end < start:
        return None
    else:
        MID_POINT = int(start + ((end - start) / 2))

        if lists[MID_POINT] > term:
            return binary_search(lists, start, MID_POINT - 1, term)
        elif lists[MID_POINT] < term:
            return binary_search(lists, MID_POINT + 1, end, term)
        else:
            return MID_POINT
