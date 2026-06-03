
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
    
def main():
    nums = [4,5,6,7,0,1,2]
    target = 0

    solution = Solution()
    print(solution.search(nums, target))

if __name__ == "__main__":
    main()
