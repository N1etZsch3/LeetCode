gas_e = [1, 2, 3, 4, 5]
cost_e = [3, 4, 5, 1, 2]


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    # 如果gas的总和小于cost总和，无论如何也到达不了
    if sum(gas) < sum(cost):
        return -1

    current_gas = 0
    start_index = 0

    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            start_index = i + 1
            current_gas = 0

    return start_index


print(can_complete_circuit(gas_e, cost_e))
