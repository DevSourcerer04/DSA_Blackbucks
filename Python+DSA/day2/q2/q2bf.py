# Find the majority element of an array
# an element is a majority element if it appears more than n/2 times in the array.
# For example, in the array [3, 3, 4], the majority element
# is 3 because it appears 2 times which is more than 3/2 = 1.5 times.
# Input: [3, 3, 4]
# Output: 3

def majority_element(arr):
    count = {}
    n = len(arr)

    for num in arr:
        count[num] = count.get(num, 0) + 1

    for num, freq in count.items():
        if freq > n / 2:
            return num

    return None

values = input("Enter array elements: ")
arr = [int(x) for x in values.replace("[", "").replace("]", "").replace(",", " ").split()]
result = majority_element(arr)
if result is not None:
    print(result)
else:
    print("-1")
