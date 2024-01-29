K, N = tuple(map(int, input().split()))

answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curr_num):
    if curr_num == N + 1:
        print_answer()
        return 
    for i in range(K):
        answer.append(i+1)
        choose(curr_num + 1)
        answer.pop()

choose(1)