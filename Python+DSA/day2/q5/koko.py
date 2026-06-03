from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                high = mid
            else:
                low = mid + 1

        return low


def main():
    piles = list(map(int, input("Enter the piles of bananas (space-separated): ").strip().split()))
    h = int(input("Enter the number of hours: ").strip())

    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    print("Minimum eating speed:", result)


if __name__ == "__main__":
    main()
