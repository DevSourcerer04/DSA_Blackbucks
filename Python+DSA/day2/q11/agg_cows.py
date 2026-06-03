class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            cows = 1
            last = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - last >= mid:
                    cows += 1
                    last = stalls[i]

            if cows >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
    
def main():
    stalls = list(map(int, input("Enter stall positions: ").strip().split()))
    k = int(input("Enter number of cows: ").strip())
    solution = Solution()
    print(solution.aggressiveCows(stalls, k))
    
if __name__ == "__main__":
    main()