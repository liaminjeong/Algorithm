import sys

K = int(input())
items = []
final_sum = 0

for _ in range(K):
    val = int(sys.stdin.readline().strip())
    if val !=0:
        items.append(val)
    else:
        items.pop()

final_sum = sum(items)
print(final_sum)
