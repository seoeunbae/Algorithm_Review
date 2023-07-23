def solution():
    sushi_count = 0
    n,d,k,c = map(int, input().split())
    plates = list(int(input()) for _ in range(n))
    result = 0
    sushi_type = [0] * (d+1)

    # 초기화
    for i in range(k):
        sushi_type[plates[i]] += 1
        if sushi_type[plates[i]] == 1:
            sushi_count += 1
    sushi_type[c] += 1
    if sushi_type[c] == 1:
        sushi_count += 1

    result = sushi_count
    for i in range(0,n):
        remove = i%n
        add = (i+k) % n

        sushi_type[plates[remove]] -= 1
        if sushi_type[plates[remove]] == 0:
            sushi_count-=1
        sushi_type[plates[add]] += 1
        if sushi_type[plates[add]] == 1:
            sushi_count+=1
        result = max(sushi_count, result)
    print(result)

solution()