def counting_sort(arr):
    if not arr:
        return []

    # Find the maximum and minimum element in the array
    max_val = max(arr)
    min_val = min(arr)

    # Create the counting array
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements

    # Count the occurrences of each element
    print("Counting occurrences:")
    for num in arr:
        count_arr[num - min_val] += 1
        print(count_arr)

    # Modify the counting array by adding the previous counts (cumulative count)
    print("\nCumulative counts:")
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
        print(count_arr)

    # Output array to store sorted elements
    output_arr = [0] * len(arr)

    # Build the output array
    print("\nBuilding the output array:")
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1
        print(output_arr)

    return output_arr

# Example usage
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original array: {arr}")

    sorted_arr = counting_sort(arr)
    print(f"\nSorted array: {sorted_arr}")
