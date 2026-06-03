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


def parse_numbers(raw: str) -> List[int]:
    raw = raw.strip()

    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]

    if not raw.strip():
        return []

    return [int(x) for x in raw.replace(",", " ").split()]


def main():
    nums = parse_numbers(input("Enter numbers: "))
    k = int(input("Enter k: ").strip())

    if len(nums) < 2:
        print("Enter at least two numbers.")
        return

    total_pairs = len(nums) * (len(nums) - 1) // 2
    if k < 1 or k > total_pairs:
        print(f"k must be between 1 and {total_pairs}.")
        return

    solution = Solution()
    print(solution.smallestDistancePair(nums, k))


if __name__ == "__main__":
    main()
