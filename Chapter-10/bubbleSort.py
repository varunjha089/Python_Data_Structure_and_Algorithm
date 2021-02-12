def bubble(lists):
    iterationNumber = len(lists) - 1
    for i in range(iterationNumber):
        for j in range(iterationNumber):
            if lists[j] > lists[j + 1]:
                temp = lists[j]
                lists[j] = lists[j + 1]
                lists[j + 1] = temp