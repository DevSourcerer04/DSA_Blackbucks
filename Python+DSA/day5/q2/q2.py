#max vowels in a substring of size k (lc1456)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        n = len(s)
        count = 0
        maxCount = 0
        left = 0
        vowels = set('aeiouAEIOU')
        for right in range(n):
            if s[right] in vowels:
                count += 1
            if right - left + 1 == k:
                if count > maxCount:
                    maxCount = count
                if s[left] in vowels:
                    count -= 1
                left += 1
        return maxCount

def main():
    s = input("Enter the string: ")
    k = int(input("Enter the value of k: "))
    sol = Solution()
    result = sol.maxVowels(s, k)
    print("The maximum number of vowels in a substring of length k is:", result)

if __name__ == "__main__":
    main()