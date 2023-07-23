# 알고리즘 리뷰 프로젝트 5-Week(7/22)

## [Baekjoon_2531] 회전초밥

난이도 : 실버

링크 : https://www.acmicpc.net/problem/2531


<br/>


### 제한사항



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

완전탐색으로, 풀이법
    - n번씩, n/k번씩 을 돌아서, 매번 set에 담아주면서, 총 최대개수를 저장한다.

시간초과가 나는 풀이법

# 다른 풀이

## sliding window로 풀이
