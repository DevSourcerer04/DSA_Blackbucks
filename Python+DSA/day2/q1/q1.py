# Array leaders: Geekforgeeks
# find the leaders in an array.
# An element is a leader if it is greater than all the elements to its right.
# For example, in the array [16, 17, 4, 3, 5, 2], the leaders are 17, 5 and 2.
# The rightmost element is always a leader.
# Input: [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Approach: We can traverse the array from right to left and keep track of the maximum element seen so far. If the current element is greater than the maximum element, it is a leader and we update the maximum element.
# Time complexity: O(n)
# Space complexity: O(n) for storing the leaders

def find_leaders(arr):
    leaders = []
    n = len(arr)
    max_so_far = float('-inf') # -infinity

    for i in range(n - 1, -1, -1):
        if arr[i] > max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]

    return leaders[::-1] 


values = input("Enter array elements: ")
arr = [int(x) for x in values.replace("[", "").replace("]", "").replace(",", " ").split()]

print("Leaders:", find_leaders(arr))
