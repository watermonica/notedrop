# ATM 1

master = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    ATMbal, trans = k, []
    people = list(map(int, input().split()))
    for i in people:
        if ATMbal == 0:
            trans.append(0)
        if ATMbal > 0:
            if (ATMbal - i) < 0:
                trans.append(0)
            if (ATMbal - i) >= 0:
                ATMbal -= i
                trans.append(1)

    master.append(trans)
x = [print(i) for i in master]


# ATM 2

def atm():
    withdraw, balance = map(float, input().split())
    if withdraw % 5 == 0:
        if balance - withdraw < 0.50:
            print('%.2f' % balance)
        else:
            balance -= withdraw + .50
            print('%.2f' % balance)
    else:
        print('%.2f' % balance)


atm()
