class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)

        total = 0
        for ele in arr:
            total += ele
        sum = 0
        for i in range(n):
            total -= arr[i]
            if sum == total:
                return i
            sum += arr[i]
        return -1
    
def main():
    arr = list(map(int, input("Enter the array elements separated by space: ").strip().split()))
    solution = Solution()
    equilibrium_index = solution.findEquilibrium(arr)
    if equilibrium_index != -1:
        print(f"Equilibrium point found at index: {equilibrium_index}")
    else:
        print("No equilibrium point found.")

if __name__ == "__main__":
    main()