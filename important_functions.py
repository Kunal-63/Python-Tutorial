def factorial(n):           # 5
    """
    This function returns factorial of the number given in the argument.
    And this is my first docstring
    """
    fact = 1
    for i in range(1, n+1):      # for i in range(1, 6): i = 1,2,3,4,5
        fact = fact * i
    return fact


def primeCheck(n):
    if n == 1: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


def armstrong(n):           # n = 153
    power = len(str(n))
    sum = 0
    for x in str(n):        # str(n) = "153"; x = "1", "5", "3"
        sum = sum + int(x) ** power
    if sum == n:
        return True
    else:
        return False


def perfectCheck(n):
    return True if sum([i for i in range(1, n) if n % i == 0]) == n else False


def avg(*args):
    return sum(args)/len(args)