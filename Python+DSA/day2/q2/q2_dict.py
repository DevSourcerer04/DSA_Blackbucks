# majority elements using dictionaries
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = dict()
        for ele in nums:
            dict1[ele] = dict1.get(ele, 0) + 1
        
        for key in dict1:
            if dict1[key] > n//2:
                return key
        return -1
    
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

    solution = Solution()
    result = solution.majorityElement(nums)
    if result != -1:
        print(result)
    else:
        print("-1")


if __name__ == "__main__":
    main()
