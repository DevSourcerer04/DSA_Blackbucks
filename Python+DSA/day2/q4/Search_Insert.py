class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


def main():
    s = input("Enter a sorted array of integers (comma-separated): ").strip()
    if s == "":
        print("No input provided.")
        return
    try:
        nums = list(map(int, s.split(',')))
    except ValueError:
        print("Invalid input. Please enter a sorted array of integers.")
        return

    target_input = input("Enter the target integer: ").strip()
    if target_input == "":
        print("No target provided.")
        return
    try:
        target = int(target_input)
    except ValueError:
        print("Invalid input. Please enter an integer for the target.")
        return

    solution = Solution()
    index = solution.searchInsert(nums, target)
    print(f"Target {target} should be inserted at index: {index}, between {nums[index-1] if index > 0 else 'start'} and {nums[index] if index < len(nums) else 'end'}.")


if __name__ == "__main__":
    main()
