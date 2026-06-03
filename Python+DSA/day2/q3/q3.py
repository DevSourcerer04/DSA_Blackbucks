# find the equilibrium point in an array
# An equilibrium point in an array is a position such that the sum of elements before it is equal to the sum of elements after it. For example, in the array [1, 3, 5, 2, 2], the equilibrium point is at index 2 (0-based) because the sum of elements before it (1 + 3) is equal to the sum of elements after it (2 + 2).

def equilibrium_point(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]  # total_sum now represents the right sum

        if left_sum == total_sum:
            return i  # Return the index of the equilibrium point

        left_sum += arr[i]  # Update left_sum for the next iteration

    return -1  # Return -1 if no equilibrium point is found