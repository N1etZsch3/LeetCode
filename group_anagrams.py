from typing import List

from black.trans import defaultdict

strs_example = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs: List[str]) -> List[List[str]]:

    d = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        d[key].append(s)

    return list(d.values())


print(group_anagrams(strs_example))
