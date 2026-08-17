def rec(num):
    if num>2:
        return  rec(num-1) + rec(num-2)
    else:
        return 1

print(rec(6))

def rece(nume):
    if nume>1:
        return nume * rece(nume-1)
    else:
        return 1

print(rece(4))

def recurring(number):
    if number > 1:
        return number * recurring(number - 1)
    else:
        return 1

print(recurring(4))