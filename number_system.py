def user_information():
    user_input_source_system = int(input("Введите исходную систему счисления: "))
    user_input_target_system = int(input("Введите целевую систему счисления: "))
    user_input_num = input("Введите число: ")
    return user_input_source_system, user_input_target_system, user_input_num

def to_decimal(num, base):
    decimal_num = 0
    power = len(num) - 1
    for digit in num:
        if digit.isdigit():
            decimal_num += int(digit) * (base ** power)
        else:
            decimal_num += (ord(digit.lower()) - ord('a') + 10) * (base ** power)
        power -= 1
    return decimal_num

def from_decimal(decimal_num, base):
    result_num = ''
    while decimal_num > 0:
        num = decimal_num % base
        if num < 10:
            result_num = str(num) + result_num
        else:
            result_num = chr(ord('a') + num - 10) + result_num
        decimal_num //= base
    return result_num if result_num else '0'

def convert_between_systems():
    user_data = user_information()
    source_system = user_data[0]
    target_system = user_data[1]
    user_num = user_data[2]

    decimal_num = to_decimal(user_num, source_system)
    result_num = from_decimal(decimal_num, target_system)
    return result_num

if __name__ == "__main__":
    result = convert_between_systems()
    print("Число в системе счисления:", result)
