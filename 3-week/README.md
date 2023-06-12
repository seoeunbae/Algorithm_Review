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

## [Baekjoon_10971] 외판원 순회2

난이도 : Silver

링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">



### 문제 설명




</div>
</details>

## 구현 풀이



