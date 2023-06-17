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

난이도 : LV.3

링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150367?language=python3

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">



### 문제 설명

당신은 이진트리를 수로 표현하는 것을 좋아합니다.
이진트리를 수로 표현하는 방법은 다음과 같습니다.
```
이진수를 저장할 빈 문자열을 생성합니다.
주어진 이진트리에 더미 노드를 추가하여 포화 이진트리로 만듭니다. 루트 노드는 그대로 유지합니다.
만들어진 포화 이진트리의 노드들을 가장 왼쪽 노드부터 가장 오른쪽 노드까지, 왼쪽에 있는 순서대로 살펴봅니다. 노드의 높이는 살펴보는 순서에 영향을 끼치지 않습니다.
살펴본 노드가 더미 노드라면, 문자열 뒤에 0을 추가합니다. 살펴본 노드가 더미 노드가 아니라면, 문자열 뒤에 1을 추가합니다.
문자열에 저장된 이진수를 십진수로 변환합니다.
```
이진트리에서 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브트리의 노드들보다 오른쪽에 있으며, 자신의 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정합니다.


주어진 이진트리에 더미노드를 추가하여 포화 이진트리로 만들면 다음과 같습니다. 더미 노드는 점선으로 표시하였고, 노드 안의 수는 살펴보는 순서를 의미합니다.


노드들을 왼쪽에 있는 순서대로 살펴보며 0과 1을 생성한 문자열에 추가하면 "0111010"이 됩니다. 이 이진수를 십진수로 변환하면 58입니다.
당신은 수가 주어졌을때, 하나의 이진트리로 해당 수를 표현할 수 있는지 알고 싶습니다.
이진트리로 만들고 싶은 수를 담은 1차원 정수 배열 numbers가 주어집니다. 
numbers에 주어진 순서대로 하나의 이진트리로 해당 수를 표현할 수 있다면 1을,
표현할 수 없다면 0을 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요.
### 제한사항

```
1 ≤ numbers의 길이 ≤ 10,000
1 ≤ numbers의 원소 ≤ 1015
```

### 입출력 예

| numbers    | result  |
|------------|---------|
| [7, 42, 5] |[1, 1, 0] |
|[63, 111, 95]|[1, 1, 0]|


</div>
</details>

## 풀이

```python
def solution(numbers):
    answer = []
    for number in numbers:
         answer.append(int(check_valid_tree(convert_to_full(to_binary(number)))))
    return answer
        
    
def to_binary(number):
    return bin(number)[2:]

#H:1, NODE: 1
#H:2, NODE: 1+2
#H:3, NODE: 1+2+4
#H:4, NODE: 1+2+4+8
def convert_to_full(binary):
    height, node  = 1, 1
    while len(binary) > node:
        height+=1
        node += 2**(height-1)
    
    return "0"*(node-len(binary))+binary

def check_valid_tree(tree):
    if len(tree) == 1:
        return True
    
    root_index = len(tree)//2
    root = tree[root_index]
    if root == "0" and not all(child == "0" for child in tree):
        return False
    # 하나라도 1이면 유효하지않음
    
    return check_valid_tree(tree[:root_index]) and check_valid_tree(tree[root_index+1:])
```

들어오는 십진수 배열에 대해서 각각
이진수 변환 -> 포화 이진 트리 변환 -> 유효성 확인 을 거친다.
- 이진수 변환 
  - 이진수 변환 값에는 0b가 앞에 붙으므로, 슬라이싱한다.
- 포화이진트리변환

  - 포화이진트리의 특징인, 높이에 해당하는 노드의 수가 정해져 있는 것을 활용한다.
  - 만들 수 있는 가장 최소 노드의 수를 찾은 뒤에
  - 해당 노드수 만큼 0를 앞에 붙인다.
- 유효성 확인
  
  - 길이가 1인 경우는 항상 True,
  - 그 외는 재귀를 활용하여, 루트가 0인 경우는 자식들도 전부 0이어야 True
  - 루트가 0일때 자식노드중에 하나라도 1인 경우는 False이다.