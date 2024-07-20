def selection_sort(arr, simulation=False):
    """ Selection Sort
        Complexity: O(n^2)
    """
    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)

    for i in range(len(arr)):
        lowestNumberIndex = i

        for j in range(i + 1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[lowestNumberIndex]:
                lowestNumberIndex = j

        if i != lowestNumberIndex:
            arr[lowestNumberIndex], arr[i] = arr[i], arr[lowestNumberIndex]

        if simulation:
            iteration = iteration + 1
            print("iteration", iteration, ":", *arr)

    return arr
