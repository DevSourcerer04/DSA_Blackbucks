from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


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
    target = int(input("Enter target: ").strip())
    solution = Solution()
    print(solution.search(nums, target))


if __name__ == "__main__":
    main()
