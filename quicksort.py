def partition(A, low, high):
	pivot = A[high]
	i = low - 1

	for j in range(low, high):
		if A[j] < pivot:
			i = i + 1
			A[i], A[j] = A[j], A[i]

	A[high], A[i + 1] = A[i + 1], A[high]
	return i + 1

def quicksort(A, low, high):
	if low < high:
		pivot = partition(A, low, high)

		quicksort(A, low, pivot - 1)
		quicksort(A, pivot + 1, high)

arr = [7, 6, 5, 4, 3, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(*arr)