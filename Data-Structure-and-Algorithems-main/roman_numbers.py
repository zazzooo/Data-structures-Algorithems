
def roman_number(n):
    result = ''
    n_str = str(n)
    if len(n_str) > 3:
        # print(n_str[:-3])
        result = int(n_str[:-3])*'M' + result
    n_str = n_str[-3:]
    # print(n_str)
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

print(roman_number(1342))
print(roman_number(9000))

def int_to_Roman(num):
    val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roman_num = ''
    i = 0
    while  num > 0:
        k = num // val[i]
        roman_num += k*syb[i]
        num -= k*val[i]
        # for k in range(num // val[i]):
        #     roman_num += syb[i]
        #     num -= val[i]
        i += 1
    return roman_num

print(int_to_Roman(1342))
print(int_to_Roman(9000))
