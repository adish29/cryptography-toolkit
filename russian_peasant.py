"""
Author : Adish Pathare
Description : Takes in two parameters in hexadecimal notation representing polynomials and print
out the resulting hex that represents the multiplication of the polynomials.
"""


def russian_peasant(value1, value2):
    left_column_value, right_column_value = value1, value2
    addition_array = []
    boundary_value = 0x7f
    while True:
        if right_column_value % 2 == 1:
            addition_array.append(int(left_column_value))
        if right_column_value == 1:
            break
        if left_column_value > boundary_value:
            left_column_value = left_column_value << 1
            left_column_value = left_column_value ^ 0x11b
        else:
            left_column_value = left_column_value << 1
        right_column_value = right_column_value >> 1

    result = addition_array[0]
    for i in range(1, len(addition_array)):
        result ^= addition_array[i]

    multiplication_value = hex(result)

    return multiplication_value


def main():
    print(russian_peasant(0x0b, 0x47))
    print(russian_peasant(0x0d, 0x37))
    print(russian_peasant(0x09, 0x94))
    print(russian_peasant(0x0e, 0xed))


if __name__ == '__main__':
    main()

"""
Answer:
Multiplication of 0x1E and 0x37 gives 0x4c
"""
