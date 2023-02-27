def bogo_sort(lst):
    count = 0
    while not is_sorted(lst):
        random.shuffle(lst)
        count += 1
    return count


def is_sorted(l):
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
    return True
