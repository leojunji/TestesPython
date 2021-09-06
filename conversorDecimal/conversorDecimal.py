def transferToDecimal(value=str, value_base=int):

    result_decimal = 0
    exponent = len(value) - 1  # here, the highest exponent will be defined(ex: 5001 = 3(highest exponent)
    lstLetters = ["A", "B", "C", "D", "E", "F"]

    for i in range(0, len(value)):

        suport_number = value[i]

        if value[i] in lstLetters:
            suport_number = hexadecimalOrdecimal(suport_number)

        result_decimal += (int(suport_number) * (value_base ** exponent))
        exponent -= 1  # decrease exponent up to 0(zero)

    return result_decimal


def transferToAnother(value, another_base):

    quotient = int(value)
    result_another = ""
    lstLetters = ["A", "B", "C", "D", "E", "F"]

    while True:
        result_temp = int(quotient % another_base)

        if result_temp > 9:
            result_temp = hexadecimalOrdecimal(result_temp)
        result_another += str(result_temp)  # it will receive the each remainder(%) of each division
        quotient = int(quotient // another_base)

        if quotient == 0:
            return result_another[::-1]  # [::-1] it will reverse the resultAnother


def hexadecimalOrdecimal(value):

    lstLetters = ["A", "B", "C", "D", "E", "F"]
    lstNumbers = [10, 11, 12, 13, 14, 15]

    if value in lstLetters:

        value = lstNumbers[lstLetters.index(value)]

    else:

        value = lstLetters[lstNumbers.index(int(value))]

    return value


while True:
    value = str(input("Enter value: ")).strip().upper()
    if value == '-1' or value == 'EXIT':
        break
    base = int(input("Enter their base: "))
    another_base = int(input("Enter another base: "))

    if another_base == 10:

        result = transferToDecimal(value, base)
        print(f"{value}[{base}] == {result}[10]")

    elif another_base != 10:
        result = transferToDecimal(value, base)
        result = transferToAnother(result, another_base)
        print(f"{value}[{base}] == {result}[{another_base}]")

    else:
        print("ERROR!!!")
