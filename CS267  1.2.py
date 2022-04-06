import time


def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


start_time = time.time()

sampleArray = [100, 45, 33, 55, 356, 11, 1000, 999, 987]
print(sampleArray)

mergeSort(sampleArray)
print("Sorted array is: ")
print(sampleArray)

# bubbleSort(sampleArray)

# print("\nSorted array is:")
# for i in range(len(sampleArray)):
#    print("%d" % sampleArray[i]),

print("--- %s seconds ---" % (time.time() - start_time))