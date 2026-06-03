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
        s = input("Enter the number of stalls and cows (space separated): ").strip()
        if s == "":
            print("No input provided.")
            return
        try:
            n, k = map(int, s.split())
        except ValueError:
            print("Invalid input. Please enter two integers.")
            return

        s = input("Enter the positions of the stalls (space separated): ").strip()
        if s == "":
            print("No input provided.")
            return
        try:
            stalls = list(map(int, s.split()))
        except ValueError:
            print("Invalid input. Please enter integers for stall positions.")
            return

        solution = Solution()
        result = solution.aggressiveCows(stalls, k)
        print("Largest minimum distance:", result)

if __name__ == "__main__":
    Solution.main()