# Minimum Number of Days to Make m Bouquets
#You are given an integer array bloomDay, an integer m and an integer k.
#You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
#Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:
            mid = (low + high) // 2

            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                high = mid
            else:
                low = mid + 1

        return low


def main():
    bloomDay = list(map(int, input("Enter bloom days (space-separated): ").strip().split()))
    m = int(input("Enter number of bouquets (m): ").strip())
    k = int(input("Enter number of adjacent flowers needed (k): ").strip())

    solution = Solution()
    result = solution.minDays(bloomDay, m, k)
    print("Minimum number of days to make m bouquets:", result)


if __name__ == "__main__":
    main()
