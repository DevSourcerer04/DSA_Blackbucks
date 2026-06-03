# Find First and Last Position of Element in Sorted Array.
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            low, high = 0, len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        def findLast():
            low, high = 0, len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        return [findFirst(), findLast()]
    
def main():
    s = input("Enter sorted array with spaces: ").strip()
    target = int(input("Enter target: ").strip())
    nums = list(map(int, s.split()))
    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)
if __name__ == "__main__":
    main()
