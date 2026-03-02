s_e = "ADOBECODEBANC"
t_e = "ABC"


def minWindow(s: str, t: str) -> str:
    need, window, valid = dict(), dict(), 0

    for c in t:
        need[c] = need.get(c, 0) + 1

    left, start, min_len = 0, 0, float("inf")

    for right in range(len(s)):
        c = s[right]

        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need):
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1

            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return "" if min_len == float("inf") else s[start : start + min_len]


print(minWindow(s_e, t_e))
