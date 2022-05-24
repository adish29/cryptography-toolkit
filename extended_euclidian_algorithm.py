"""
filename : extended_euclidian_algorithm.py
Author : Adish Pathare
Description: Calculate multiplicative inverse of a mod b.
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extented_euclidian_algorithm(a, b):
    q = []
    x = 0
    b_original = b
    while a != 1:
        temp = a // b
        q.append(temp)
        r = a % b
        a = b
        b = r
    xc = a
    yc = b
    for i in range(len(q)-1, -1, -1):
        x = yc
        y = xc - (yc * q[i])
        xc = x
        yc = y
    print(x % b_original)


def main():
    print("Enter the value of a:")
    a = int(input().strip())
    print("Enter the value of b:")
    b = int(input().strip())
    if gcd(a, b) != 1:
        print("Inverse does not exist as gcd is not 1")
        print("GCD is ", gcd(a, b))
    else:
        print("The inverse of %d mod %d is:" % (a, b))
        extented_euclidian_algorithm(a, b)
        print("Do you also wish to know inverse of %d mod %d? Enter 1 if yes and anything random to exit" % (b, a))
        flag = input()
        if flag == '1':
            print("The inverse of %d mod %d is:" % (b, a))
            extented_euclidian_algorithm(b, a)


if __name__ == '__main__':
    main()

"""
find the inverse of 7111111 mod 123456.
Answer : 34807
"""