K, N = tuple(map(int, input().split()))
selected_nums = []

def print_permutation():
    for elem in selected_nums:
        print(elem, end = " ")
    print()

def find_permutation(cnt):
    if cnt == N:
        print_permutation()
        return
    
    for i in range(1, K + 1):
        if cnt >= 2 and selected_nums[-1] == i and selected_nums[-2] == i:
            continue
        
        selected_nums.append(i)
        find_permutation(cnt + 1)
        selected_nums.pop()
find_permutation(0)