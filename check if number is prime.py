def isPrime(number):
    if number == 2:
        return True
    if number == 1:
        return False
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number %3 == 0:
        return False
    i=5
    w=2
    while i*i <= number:
        if number% i == 0:
            return False
        i+=w
        w=6-w
    return True
x=isPrime(7)
print(x)