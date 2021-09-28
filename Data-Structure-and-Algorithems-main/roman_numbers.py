
def roman_number(n):
    result = ''
    n_str = str(n)
    for i in range(len(n_str)):
        cifra = int(n_str[i])
        print(cifra)
        if cifra > 5:
            result = result + 'V'
            cifra -= 5
        print(cifra)
        result = result + cifra*'I'
    return result

print(roman_number(45))
