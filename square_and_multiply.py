"""
Author : Adish Pathare
Description : Implement pseudo code for square and multiply algorithm
"""


def square_multiply(value, power, mod):
    # binary conversion of power value
    # The binary value is in form of string
    binary_value = f"{power:b}"
    answer = 0

    for i in range(len(binary_value)):
        if i == 0:
            answer = value
        else:
            bit = binary_value[i]
            answer = (answer ** 2) % mod
            if bit == '1':
                answer = (answer * value) % mod

    return answer


def main():
    # print(square_multiply(1234567, 23456789, 3333337))
    print(square_multiply(51, 167, 467))


if __name__ == '__main__':
    main()

"""
Use your program to calculate 1234567^23456789 mod 3333337
Answer : 1138812
"""