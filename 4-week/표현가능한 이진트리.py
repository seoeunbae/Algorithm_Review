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