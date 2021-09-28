
def roman_number(n):
    result = ''
    n_str = str(n)
    if len(n_str) > 3:
        # print(n_str[:-3])
        result = int(n_str[:-3])*'M' + result
    n_str = n_str[-3:]
    print(n_str)
    for i in range(len(n_str)):
        # print(i,len(n_str))
        if i == len(n_str)-1:
            cifra = int(n_str[i])
            if cifra >= 5:
                result = result + 'V'
                cifra -= 5
            result = result + cifra*'I'
        if i == len(n_str)-2:
            cifra = int(n_str[i])
            # print(cifra)
            if cifra >= 5:
                result = result + 'L'
                cifra -= 5
            result = result + cifra*'X'
        if i == len(n_str)-3:
            cifra = int(n_str[i])
            if cifra >= 5:
                result = result + 'D'
                cifra -= 5
            result = result + cifra*'C'
        if i == len(n_str)-4:
            break
    return result

print(roman_number(2736))
