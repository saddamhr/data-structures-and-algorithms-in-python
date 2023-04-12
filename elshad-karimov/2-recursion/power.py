def power(base, exp):
    # assert int(exp) == exp, 'The exponent must be integer number only!'
    if exp == 0:
        return 1
    elif base ==0:
        return 0
    elif exp < 0:
        return 1 / base * power(base, exp + 1)
    return  base * power(base, exp-1)


print(power(0.00001,
2147483647))