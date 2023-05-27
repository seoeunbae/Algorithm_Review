from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    total_sum = queue1_sum+queue2_sum

    if total_sum % 2 == 1:
        return -1


    execute = 0
    count = 0
    while queue1_sum != queue2_sum:
        execute += 1
        # 시간초과 방지하기
        if execute > 599999:
            return -1

        if queue1 and queue1_sum > queue2_sum:
            poped = queue1.popleft()
            queue2.append(poped)
            count+=1
            queue1_sum -= poped
            queue2_sum += poped
        elif queue2 and queue2_sum > queue1_sum:
            poped = queue2.popleft()
            queue1.append(poped)
            count+=1
            queue1_sum += poped
            queue2_sum -= poped

    return count
