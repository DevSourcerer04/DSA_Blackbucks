# Find All Anagrams in a String using list frequency counts

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window_count = [0] * 26
        result = []
        left = 0
        k = len(p)

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for right in range(len(s)):
            right_index = ord(s[right]) - ord('a')
            window_count[right_index] += 1

            if right - left + 1 == k:
                if window_count == p_count:
                    result.append(left)

                left_index = ord(s[left]) - ord('a')
                window_count[left_index] -= 1
                left += 1

        return result


def main():
    s = input("Enter the string: ")
    p = input("Enter the pattern: ")

    solution = Solution()
    result = solution.findAnagrams(s, p)

    print("The starting indices of anagrams of p in s are:", result)


if __name__ == "__main__":
    main()
