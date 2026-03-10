def roman_to_int(s: str) -> int:
    # 构建字典
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    n = len(s)

    for i in range(n):
        value = roman_map[s[i]]
        # 同样判断是否小于右侧数值
        if i < n - 1 and value < roman_map[s[i + 1]]:
            total -= value
        else:
            total += value

    return total
