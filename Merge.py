def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage
unsorted_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(unsorted_array.copy())

print(f"Unsorted Array: {unsorted_array}")
print(f"Sorted Array: {sorted_array}")
