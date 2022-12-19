from collections import Counter

shoe_count = int(input())
shoe_sizes = Counter(list(map(int, input().split())))
income = 0

for _ in range(int(input())):
    shoe, cost = map(int, input().split())
    if shoe_sizes[shoe] > 0:
        shoe_sizes[shoe] -= 1
        income += cost
    else:
        continue

print(income)