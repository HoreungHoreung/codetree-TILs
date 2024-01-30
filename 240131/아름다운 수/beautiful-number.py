n = int(input())
ans = 0
cnt = []


def is_beautiful():
    i = 0
    while i < n:
        if i + cnt[i] - 1 >= n:
            return False

        for j in range(i, i + cnt[i]):
            if cnt[j] != cnt[i]:
                return False
        i += cnt[i]

    return True

def count_beautiful_seq(num):
    global ans
    
    if num == n:
        if is_beautiful():
            ans += 1
        return

    for i in range(1, 5):
        cnt.append(i)
        count_beautiful_seq(num + 1)
        cnt.pop()

count_beautiful_seq(0)
print(ans)