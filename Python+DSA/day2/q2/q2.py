# Find the majority element of an array
# an element is a majority element if it appears more than n/2 times in the array.
# For example, in the array [3, 3, 4], the majority element
# is 3 because it appears 2 times which is more than 3/2 = 1.5 times.
# Input: [3, 3, 4]
# Output: 3
# Approach: We can use the Boyer-Moore Voting Algorithm which is an efficient algorithm to find the majority element in linear time and constant space. The algorithm works by maintaining a count of the current candidate for majority element and updating it as we iterate through the array. If the count drops to zero, we select a new candidate. Finally, we verify if the candidate is indeed the majority element by counting its occurrences in the array.

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None

def main():
    try:
        s = input("Enter a list of integers (comma separated): ").strip()
        if s == "":
            print("No input provided.")
            return
        nums = list(map(int, s.split(',')))
    except ValueError:
        print("Invalid input. Please enter a list of integers.")
        return

    result = majority_element(nums)
    if result is not None:
        print(result)
    else:
        print("-1")
