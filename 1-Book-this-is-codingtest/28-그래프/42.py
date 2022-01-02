# [탑승구] 도킹가능한 비행기수 (서로소집합)

# (아이디어) 탑승구 중 가장 큰 위치에 도킹시키고, 해당 탑승구를 서로소집합에 추가한다

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


gate = int(input())
plain = int(input())
docking = [int(input()) for _ in range(plain)]

parent = list(range(gate + 1))

count = 0
for x in docking:
    root = find(x)
    if root == 0:  # 루트가 0이면 도킹 가능한 답승구가 없는 셈이다
        break

    union(root, root - 1)
    count += 1

print(count)
