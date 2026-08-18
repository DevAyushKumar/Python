def rec(num):
    if (num > 1):
        return rec(num - 1) + rec(num - 2)
    else:
        return 1

print(rec(5))