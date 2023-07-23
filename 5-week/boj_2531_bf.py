def solution():
    n,d,k,c = map(int, input().split())
    plates = list(int(input()) for _ in range(n))
    result = 0

    for i in range(n):
        each_eating = []
        for j in range (i, i+k):
            each_eating.append(plates[j%n])
        each_eating.append(c)
        sushi_count = len(set(each_eating))
        result = max(sushi_count, result)
    print(result)

solution()