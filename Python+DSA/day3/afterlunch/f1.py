from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        diff = [0] * n

        for first, last, seats in bookings:

            diff[first - 1] += seats

            if last < n:
                diff[last] -= seats

        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff

def main():
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5

    solution = Solution()
    print(solution.corpFlightBookings(bookings, n))

if __name__ == "__main__":
    main()