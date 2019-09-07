def get_summ(one, two, delimeter='&'):
    one = str(one)
    two = str(two)
    delimeter = str(delimeter)
    sum_ = one + delimeter + two
    return sum_

print(get_summ('Learn', 'Python'))
