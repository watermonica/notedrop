for _ in range(int(input())):
    a, seta = int(input()), set(list(map(int, input().split())))
    b, setb = int(input()), set(list(map(int, input().split())))
    count = 1

    y = [1 for char in seta if char in setb]
    x = [print('True') if sum(y) == a else print('False')]

    # using 'issubset'
    z = [print('True') if seta.issubset(setb) else print('False')]

