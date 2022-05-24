"""
Sample run:
input cipher text = gjxy
output plaintext = best
"""

import enchant
d = enchant.Dict("en_US")


def shift_cipher(s):
    x = []
    for val in s:
        x.append(ord(val))
    y = []
    for j in range(len(x)):
        y.append(0)
    shift = 1
    while shift < 27:
        for i in range(len(x)):
            y[i] = x[i] + shift
            if y[i] > 122:
                temp = y[i] - 122
                y[i] = 96 + temp
        word = ''
        for val in y:
            word += chr(val)
        if d.check(word):
            print(word)
        shift += 1


def main():
    s = input().strip()
    shift_cipher(s)


if __name__ == '__main__':
    main()
