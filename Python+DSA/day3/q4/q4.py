# Find minimun in reversed sorted array.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
    
def parse_nums(raw: str) -> List[int]:
    raw = raw.strip()

    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
        if not raw.strip():
            return []
        return [int(x.strip()) for x in raw.split(",")]

    if not raw:
        return []

    return [int(x) for x in raw.replace(",", " ").split()]

def main():
    nums = parse_nums(input("Enter array: "))
    solution = Solution()
    print(solution.findMin(nums))

if __name__ == "__main__":
    main()