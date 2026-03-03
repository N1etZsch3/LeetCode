intervals_e = [[1, 3], [2, 6], [8, 10], [15, 18]]


def merge(intervals: list[list[int]]) -> list[list[int]]:

    # 先给数组排序
    intervals.sort(key=lambda x: x[0])

    merged: list[list[int]] = []

    # 遍历intervals
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


print(merge(intervals_e))
