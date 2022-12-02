master = []

for _ in range(int(input())):
    num = list(input())
    num.reverse()
    master.append(int(''.join(num)))

x = [print(i) for i in master]
