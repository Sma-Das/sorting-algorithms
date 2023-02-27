def swapPositions(list, posA, posB):
    list[posA], list[posB] = list[posB], list[posA]
    return list


def gnomeSort(listToBeSorted):
    position = 0
    while position < len(listToBeSorted):
        if position == 0 or listToBeSorted[position] >= listToBeSorted[position - 1]:
            position = position + 1
        else:
            swapPositions(listToBeSorted, position, position - 1)
            position = position - 1

    return listToBeSorted
