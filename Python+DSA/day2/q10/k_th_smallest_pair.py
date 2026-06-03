from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            count = 0
            left = 0

            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1

                count += right - left

            if count >= k:
                high = mid
            else:
                low = mid + 1

        return low


def main():
    nums = list(map(int, input("Enter the list of numbers (space-separated): ").strip().split()))
    k = int(input("Enter the value of k: ").strip())

    total_pairs = len(nums) * (len(nums) - 1) // 2
    if k < 1 or k > total_pairs:
        print("Invalid k. It should be between 1 and", total_pairs)
        return

    solution = Solution()
    result = solution.smallestDistancePair(nums, k)
    print("The k-th smallest distance pair is:", result)


if __name__ == "__main__":
    main()
