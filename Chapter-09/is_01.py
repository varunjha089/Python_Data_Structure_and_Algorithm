def nearest_mid(lists, start, end, value):
    return int(start + (( end - start) / (lists[end] - lists[start] )) * ( value - lists[start]))
