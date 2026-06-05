# Find All Anagrams in a String

def findAnagrams(s: str, p: str) -> list[int]:
    p_count = {}
    s_count = {}
    result = []
    left = 0
    k = len(p)

    for ch in p:
        p_count[ch] = p_count.get(ch, 0) + 1

    for right in range(len(s)):
        s_count[s[right]] = s_count.get(s[right], 0) + 1

        if right - left + 1 == k:
            if s_count == p_count:
                result.append(left)

            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]

            left += 1

    return result

def main():
    s = input("Enter the string: ")
    p = input("Enter the pattern: ")
    result = findAnagrams(s, p)
    print("The starting indices of anagrams of p in s are:", result)

if __name__ == "__main__":
    main()