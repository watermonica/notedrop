a = set(map(int, input().split()))
n = int(input())

y = [1 for _ in range(n) if a.issuperset(set(map(int, input().split())))]
x = [print('True') if len(y) == n else print('False')]

