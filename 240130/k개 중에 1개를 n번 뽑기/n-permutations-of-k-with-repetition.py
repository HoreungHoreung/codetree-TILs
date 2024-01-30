K, N = tuple(map(int, input().split()))

selected_nums = []

def print_nums():
    for elem in selected_nums:
        print(elem, end = " ")
    print()

def find_nums(curr_num):
    if curr_num >= N + 1:
        print_nums()
        return

    for i in range(K):
        selected_nums.append(i)
        print_nums(curr_num + 1)
        selected_nums.pop()



find_nums(1)