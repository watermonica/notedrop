e, e1, f, f1 = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
print(len(set(e1).symmetric_difference(f1)))
