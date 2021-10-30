def quick_sort(arr, start, end):
	if(start < end):
		p_index = partition(arr, start, end)
		quick_sort(arr, start, p_index-1)
		quick_sort(arr, p_index+1, end)

def partition(arr, start, end):
	pivot = arr[end]
	p_index = start
	for i in range(start, end):
		if(pivot > arr[i]):
			arr[i], arr[p_index] = arr[p_index], arr[i]
			p_index += 1
	arr[p_index], arr[end] = arr[end], arr[p_index]
	return p_index

unsorted_arr = [3,45,1,3,5,75,23,45,67,22]
quick_sort(unsorted_arr, 0, len(unsorted_arr)-1)
print(unsorted_arr)
