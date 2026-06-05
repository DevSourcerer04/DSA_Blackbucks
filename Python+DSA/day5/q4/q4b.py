# Find All Anagrams in a String using dictionary frequency counts

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = {}
        window_count = {}
        result = []
        left = 0
        k = len(p)

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        for right in range(len(s)):
            right_char = s[right]
            window_count[right_char] = window_count.get(right_char, 0) + 1

            if right - left + 1 == k:
                if window_count == p_count:
                    result.append(left)

                left_char = s[left]
                window_count[left_char] -= 1

                if window_count[left_char] == 0:
                    del window_count[left_char]

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
