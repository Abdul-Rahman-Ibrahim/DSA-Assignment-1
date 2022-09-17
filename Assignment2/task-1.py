#STUDENT 340
def find_max_ind(arr):
    """

    :param arr: Array of integers
    :return: Index of the maximum
    """
    # TODO: write program that returns the index of the maximum.
    j = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[j]:
            j = i
    return j


if __name__ == "__main__":
    # get input array
    arr = list(map(int, input().rstrip().split(' ')))

    # print maximum value of array
    print(find_max_ind(arr))
