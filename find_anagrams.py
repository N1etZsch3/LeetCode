from typing import List

from collections import Counter

s_example = "cbaebabacd"
p_example = "abc"


def find_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    p_cnt = Counter(p)
    s_cnt = Counter(s[: len(p)])
    res = [0] if s_cnt == p_cnt else []

    for i in range(len(p), len(s)):
        s_cnt[s[i]] += 1  # 右边进
        s_cnt[s[i - len(p)]] -= 1  # 左边出
        if s_cnt[s[i - len(p)]] == 0:
            del s_cnt[s[i - len(p)]]
        if s_cnt == p_cnt:
            res.append(i - len(p) + 1)

    return res


print(find_anagrams(s_example, p_example))
