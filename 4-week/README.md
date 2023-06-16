# 알고리즘 리뷰 프로젝트 4-Week(6/18)

## [Leetcode_15] 3sum
- 난이도 : Medium
- 링크 : https://leetcode.com/problems/3sum/

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">

### 문제 설명

Given an integer array nums, return all the triplets ```[nums[i], nums[j], nums[k]]``` such that ```i != j```, ```i != k```, and ```j != k```, and ```nums[i] + nums[j] + nums[k] == 0```.

Notice that the solution set must not contain duplicate triplets.



### Example 1:

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

</div>
</details>

## 1. two_pointer로 풀이하는 경우

```python
class Solution(object):
    def return_list(self, start,nums):
        end = len(nums) - 1
        middle = start + 1
        # end는 내부 while문에서 관리(증가시킨다.)
        while start < end:
            # 1. 포인터가 겹칠때, return
            if start >= end or middle >= end:
                return
            # 2. 중복된 마지막 값 일때, return
            if  end < len(nums)-1 and nums[end] == nums[end+1]:
                end -= 1
                continue
            # 3. 중복된 시작값 일때, return
            if  start > 0 and nums[start] == nums[start-1]:
                return

            if nums[start] + nums[end] + nums[middle] < 0:
                middle += 1
            elif nums[start] + nums[end] + nums[middle] > 0:
                end -= 1
            else:
                # = 0인 경우
                result.append([nums[start], nums[middle], nums[end]])
                end -= 1
                continue

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        global result
        result = list()

        nums.sort()

        if nums[-1] == 0:
            zero_idx = nums.index(0)
            if zero_idx + 3 > len(nums):
                return []
            else :
                return [[0, 0, 0]]
        elif nums[-1] < 0:
            return []
        # start는 전체 for문에서 관리(증가시킨다)
        for i in range(len(nums)):
            self.return_list(i,nums)


        return result
```

3값의 합이 0인 경우를 구하는 문제 이므로, 투포인터를 활용한다.
정렬을 하고 제일 작은 값을 start 값으로 설정,
바로 두번째 값을 middle로 설정, 
제일 큰 값을 end로 설정한뒤,
0보다 크거나 작거나 여부를 통해서 middle과 end를 변동시키면서 sum 조합을 찾는다. 

start값은 ```전체반복문```에서만 점차 end로 향하도록 이동시킨다.
중복되는 경우를 없애줘야 하기때문에,
```이전 end값 == 현재 end값``` 이거나 이전 ```start값 == 현재 start값``` 인 경우, 중지한다.

배열이 음수와 0으로만 이루어진 경우, if 분기문으로,
0이 3개이상인 경우, ```[0,0,0]```을 리턴하고, 0이 3개 미만인 경우 빈 리스트를 리턴하도록 한다.

<br/>


<br/>


<br/>

## [2023kakaoblind] 표현 가능한 이진트리

난이도 : 

링크 : 

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">



### 문제 설명



</div>
</details>

## 풀이

```python

```


