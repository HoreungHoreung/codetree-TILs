K, N = tuple(map(int, input().split()))
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curr_num):
    if curr_num == N:
        print_answer()
        return
    
    for i in range(1, K + 1):
        if curr_num == 0 or curr_num == 1 or (answer[-1] != i or answer[-2] != i):
            answer.append(i)
            choose(curr_num + 1)
            answer.pop()
    
    return

choose(0)