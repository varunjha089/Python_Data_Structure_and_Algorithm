from is_01 import *

def interpolation_search(lists, term):
    size = len(lists) - 1

    start = 0
    end = size

    while start < end:
        mid_point = nearest_mid(lists, start, end, term)

        if mid_point > end or mid_point < start:
            return None

        if lists[mid_point] == term:
            start = mid_point + 1
        else:
            end = mid_point - 1
        
        if start > end:
            return None
