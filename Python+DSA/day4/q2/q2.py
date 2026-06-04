#two sum
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total < target:
                left += 1

            else:
                right -= 1

        return [-1, -1]

def main():
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target))
if __name__ == "__main__":
    main()
    