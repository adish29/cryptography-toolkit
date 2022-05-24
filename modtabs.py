def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def orderCalculator(n):
    print("n is", n)
    for i in range(1, n):
        a = i
        if gcd(a, n) != 1:
            print("GCD for a = %d = %d " % (a, gcd(a, n)))
        else:
            for k in range(1, n):
                temp = a ** k
                if temp % n == 1:
                    order = k
                    print("Order for a = %d is %d" % (a, order))
                    break


def main():
    n = int(input())
    orderCalculator(n)


if __name__ == '__main__':
    main()
