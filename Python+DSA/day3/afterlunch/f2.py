from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        current = 0

        for x in diff:
            current += x

            if current > capacity:
                return False

        return True

def main():
    s = Solution()
    print(s.carPooling([[2,1,5],[3,3,7]], 4))
    print(s.carPooling([[2,1,5],[3,3,7]], 5))
    print(s.carPooling([[2,1,5],[3,5,7]], 3))
if __name__ == "__main__":
    main()
    