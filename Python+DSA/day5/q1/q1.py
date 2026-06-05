class solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        sum = 0
        maxSum = float('-inf')
        left = 0
        for right in range(n):
            sum += nums[right]
            if right - left + 1 == k:
                if sum > maxSum:
                    sum = maxSum
                sum -= nums[left]
                left += 1
        return maxSum / k
    
def main():
    nums = input("Enter the array of integers: ")
    nums = list(map(int, nums.split()))
    k = int(input("Enter the value of k: "))
    sol = solution()
    result = sol.findMaxAverage(nums, k)
    print("The maximum average of a subarray of length k is:", result)

if __name__ == "__main__":
    main()