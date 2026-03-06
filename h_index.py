citations_e = [3, 0, 6, 1, 5]


def h_index(citations: list[int]) -> int:
    n = len(citations)

    # 建一个长度为n + 1的桶
    buckets = [0] * (n + 1)

    for c in citations:
        if c >= n:
            buckets[n] += 1
        else:
            buckets[c] += 1

    papers_count = 0
    for i in range(n, -1, -1):
        papers_count += buckets[i]
        if papers_count >= i:
            return i
    return 0


print(h_index(citations_e))
