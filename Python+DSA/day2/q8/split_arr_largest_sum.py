#Split Array Largest Sum
#Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
#Return the minimized largest sum of the split.
#A subarray is a contiguous part of the array.

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = 0

                current_sum += num

            if subarrays <= k:
                high = mid
            else:
                low = mid + 1

        return low
def main():
    nums = list(map(int, input("Enter the array of integers (space-separated): ").strip().split()))
    k = int(input("Enter the number of subarrays (k): ").strip())

    solution = Solution()
    result = solution.splitArray(nums, k)
    print("Minimized largest sum of the split:", result)


if __name__ == "__main__":
    main()
