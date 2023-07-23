# 알고리즘 리뷰 프로젝트 5-Week(7/22)

## [Baekjoon_2531] 회전초밥

난이도 : 실버

링크 : https://www.acmicpc.net/problem/2531


<br/>

### 입출력 예
- 입력
```commandline
8 30 4 30
7
9
7
30
2
7
9
25
```
- 출력
```commandline
5
```

## brute force 로 풀이

```python
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

# 시간초과
```

완전탐색으로, 풀이법 <br/>
    - n번씩, n/k번씩 을 돌아서, 매번 set에 담아주면서, 총 최대개수를 저장한다.

시간초과가 나는 풀이법

# 다른 풀이

## sliding window로 풀이
```commandline
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
```

<br/>

헤매었던 부분은,
"전체 초밥 종류 배열에 1을 더해주는 로직"과, "초밥종류개수를 +/-1해주는 로직"의 순서이다.
- 먼저 if문으로 +/- 해주기 전에 상태에 따라서 값을 변동시켜주면,
- 아래와 같은 예외 케이스에서 오답이 나온다.

<br/>

```commandline
8 30 4 30
7
7
3
7
7
8
7
7
-> 정답 : 4 / 오답 : 3
```

<br/>

**왜냐하면, 동일한 7이 2개있음에도, 이전로직에서 (배열상태를 조건으로 주고) 한번만 넣어줬기 때문에,
이번 로직에서는 7을 한번 제거하면, 0개가 존재하는 잘못된 상태가 되어버린다.**

