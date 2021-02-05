def binary_search(lists, term):
    SIZE_OF_LIST = len(lists) - 1

    START = 0
    FINISH = SIZE_OF_LIS

    while START <= FINISH:
        MID_POINT = (START + FINISH)
        
        if lists[MID_POINT] == term:
            return MID_POINT
        
        if term > lists[MID_POINT]:
            START = MID_POINT + 1
        else:
            FINISH = MID_POINT - 1

    if START > FINISH:
        return None