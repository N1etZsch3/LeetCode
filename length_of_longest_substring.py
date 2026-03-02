s_example = "pwwkew"


def length_of_longest_substring(s: str) -> int:
    window = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])

        max_len = max(max_len, right - left + 1)

    return max_len


print(length_of_longest_substring(s_example))
