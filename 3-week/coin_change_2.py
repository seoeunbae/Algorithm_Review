def count_case_coin_changing(coins, t, case):
    case[0] = 1
    for c in coins:
        for j in range(c, t+1):
            case[j] += case[j-c]

    return case


def solution():
    coins = [1,2,5]
    t = 5
    case = [0 for _ in range(t+1)]
    answer = count_case_coin_changing(coins, t, case)
    return answer[t]


solution()