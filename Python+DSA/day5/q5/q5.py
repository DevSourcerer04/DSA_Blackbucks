class Solution:
    def firstNegInt(self, arr, k):
        q = []
        front = 0
        ans = []

        for i in range(len(arr)):

            if arr[i] < 0:
                q.append(i)

            if i >= k - 1:

                while front < len(q) and q[front] <= i - k:
                    front += 1

                if front < len(q):
                    ans.append(arr[q[front]])
                else:
                    ans.append(0)

        return ans
    
    def main():
        arr = input("Enter the array: ").split()
        arr = list(map(int, arr))
        k = int(input("Enter the value of k: "))
        solution = Solution()
        result = solution.firstNegInt(arr, k)
        print("First negative integer in every window of size k:", result)
    if __name__ == "__main__":
        main()