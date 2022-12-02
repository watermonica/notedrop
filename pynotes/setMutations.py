len_seta = int(input())
seta = set(list(map(int, input().split())))

for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(seta, cmd)(set(list(map(int, input().split()))))
print(sum(seta))

