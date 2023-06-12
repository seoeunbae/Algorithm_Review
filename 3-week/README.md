# 알고리즘 리뷰 프로젝트 3-Week(6/11)

## [Leetcode_518] Coin Change 2
- 난이도 : Medium
- 링크 : https://leetcode.com/problems/coin-change-ii/

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">

### 문제 설명

You are given an ```integer``` array coins representing coins of different denominations and an ```integer``` amount representing a total amount of money.

Return ```the number of combinations``` that make up that amount. If that amount of money cannot be made up by any combination of the coins, return ```0```.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.



### Example 1:
```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

</div>
</details>

## 1. Backtracking로 풀이하는 경우

```java
import java.util.*;

public class LeetCode_coinchange2 {
    public static void main(String[] args) {
        int count = change(5, new int[]{1, 2, 5});
        System.out.println(count);
    }

    public static int change(int amount, int[] coins) {
        List<List<Integer>> combinations = new ArrayList<>();
        backtrack(combinations, new ArrayList<>(), amount, coins, 0);
        return combinations.size();
    }

    public static void backtrack(List<List<Integer>> combinations, List<Integer> current, int remaining, int[] coins, int start) {
        if (remaining == 0) {
            System.out.println(current);
            combinations.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < coins.length; i++) {
            if (remaining - coins[i] >= 0) {
                current.add(coins[i]);
                backtrack(combinations, current, remaining - coins[i], coins, i);
                current.remove(current.size() - 1);
            }
        }
    }
}

```

백트래킹을 통해서 남은 정수가 없을때, combinations리스트에 각 완성된 리스트를 넣어준다.
만약에, 각 백트래킹이 도는 반복문의 시작점을 0으로 통일하면, 순서가 다를때 다른 케이스으로 인지해서,
**1,2,3**과 **1,3,2**를 다른 케이스로 인지한다.
즉, 정답 보다 더 많은 양의 리스트가 담겨진다.

<br/>

이를 방지하기 위해, 반복문의 시작점을 업데이트해서 재귀를 돌려준다.
그러면, 이전에 담긴 요소는 제외되고 반복문이 돌기 때문에, (순서만 다르고)같은 경우들이 하나의 케이스로 담겨진다.
그러나 위 방법은 **Time Limit Exceeded** 가 되었다.

<br/>

## 2. DP로 풀이하는 경우

```python
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

```

DP와 메모이제이션을 활용한다.
case크기는 amount의 크기와 동일하고, 각 ```case[amount]```는 해당 amount를 만들 수 있는 총 경우의 수가 들어간다.
coins배열을 반복문으로 돌면서, 각 코인이 해당 amount를 만들 수 있는 경우의 수를
작은 코인부터 더해준다.
<br/>

이때, **만약 코인이 3인 경우, ```각amount-3이 만들어지는 경우의 수```가 그대로 전달되면 되므로
j-c의 경우의 수를 j의 경우의 수에 더해 주는 것이다.** [위에서 j는 각 amount에 해당, c는 각 코인에 해당]

<br/>

## [Baekjoon_14501] 퇴사

난이도 : Silver 3

링크 : https://www.acmicpc.net/problem/14501

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">



### 문제 설명

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

|     | 1일  | 2일  |3일|4일|5일|6일|7일|
|-----|---|-----|---|---|---|---|---|
| Ti	 |3| 5   |1|1|2|4|2|
| Pi	 |10| 20  |10|20|15|40|200|
1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

---

### 입력

---

첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

### 출력

첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

---

### 예시

---

```
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
```

```
45
```

---

</div>
</details>

## DP 풀이

```python
import sys

def solution():
    n = int(input())
    T = []
    P = []
    answer = [0 for _ in range(n+1)]
    for _ in range(n):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)


    for i in range(n-1, -1, -1):
        if i + T[i] > n:
            answer[i] = answer[i+1]
            continue
        else:
            if T[i] == 1:
                answer[i] = P[i] + answer[i+1]
                continue
            # answer[i] = max(answer[i+1], answer[i + T[i] ] + P[i])
            elif answer[i+1] < answer[i+T[i]] + P[i]:
                answer[i] = P[i] + answer[i+T[i]]
            else:
                answer[i] = answer[i] + answer[i+1]
    print(answer[0])
```

T 는 i번째 일을 완료하는데 걸리는 시간
P 는 i번째 일을 완료하면 받는 금액
answer는 마지막날짜부터 거꾸로 계산한, 해당 날짜의 최대이익이다.
[i번쨰 일 소요시간 + i]의 최대이익 + i번쨰의 이익 vs i+1번쨰의 최대이익을 비교한뒤에
더 큰 이익을 낼 수 있는 값을 갱신한다.
