#linear search
def naive_Search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None

#binary search
def binary_Search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None 

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print(naive_Search(my_list, 3))
    print(binary_Search(my_list, 3))