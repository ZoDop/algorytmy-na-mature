def binary_search_iteracyjnie(list, s): #s - co szukamy
    first = 0
    last = len(list)
    while first <= last:
        middle = (first + last) // 2
        if list[middle] == s:
            return middle
        elif list[middle] < s:
            first = middle + 1
        else:
            last = middle - 1
    return -1

def binary_search_rekurencyjnie(list, s, first, last):
    if first <= last:
        middle = (first + last) // 2
        if list[middle] == s:
            return middle
        elif list[middle] < s:
            return binary_search_rekurencyjnie(list, s , middle + 1 ,last)
        else:
            return binary_search_rekurencyjnie(list ,s, first ,middle - 1)
    return -1

def binary_search_rekurencyjnie_by_mr_Budniak(list, s, first, last):
    if first > last:
        return -1
    middle = (first + last) // 2
    if list[middle] == s:
        return middle
    elif list[middle] < s:
        return binary_search_rekurencyjnie(list, s , middle + 1 ,last)
    else:
        return binary_search_rekurencyjnie(list ,s, first ,middle - 1)



