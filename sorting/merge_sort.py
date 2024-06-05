def merge_sort(arr):
	len_arr = len(arr)
	if(len_arr <= 1):
		return arr
	mid = len_arr // 2
	left = arr[:mid]
	right = arr[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return combine_two_array(left, right)

def combine_two_array(arr_a, arr_b):
	sorted_arr = []
	len_a = len(arr_a)
	len_b = len(arr_b)
	i = j = 0
	while(i < len_a and j < len_b):
		if(arr_a[i] < arr_b[j]):
			sorted_arr.append(arr_a[i])
			i += 1
		else:
			sorted_arr.append(arr_b[j])
			j += 1
	while(i < len_a):
		sorted_arr.append(arr_a[i])
		i += 1
	while(j < len_b):
		sorted_arr.append(arr_b[j])
		j += 1
	return sorted_arr
