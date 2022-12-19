# Karatsuba Multiplication


# only accepts 4
def karatsuba4(x, y):
    x, y = str(x), str(y)
    if len(x) != 4 or len(y) != 4:
        raise Exception('invalid input, x&y must be even and == 4')
    elif len(x) % 2 == 0 and len(y) % 2 == 0:
        a, b, c, d = int(x[:2]), int(x[2:]), int(y[:2]), int(y[2:])

        step1 = a*c
        step2 = b*d
        step3 = (a+b)*(c+d)
        step4 = step3 - step2 - step1

        new1 = step1 * (10**5)
        new2 = step2
        new4 = step4 * (10**3)

        print(new1+new2+new4)
    else:
        raise Exception('invalid input, N must be even and == 4')


num1, num2 = map(int, input().split())
karatsuba4(num1, num2)
