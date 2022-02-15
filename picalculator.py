import math

def newtonPi(init):
    next1 = init - (math.sin(init)/math.cos(init))
    next2 = next1 - (math.sin(next1)/math.cos(next1))
    next3 = next2 - (math.sin(next2) / math.cos(next2))
    return next3





def leibnizPi(iterations):
    result = 0
    numerator = 1
    denominator = 1

    for i in range(iterations):
        result = result + (numerator/denominator)
        numerator *= -1
        denominator += 2

    result *= 4
    return result

def nilakanthaPi(n):
    starter = 3.0
    if n==1:
        return starter
    elif n>1:
        a = 0.0
        first = 1
        result = 3.0
        denominator = 2
        for i in range(n-1):
            a += first/((denominator)*(denominator+1)*(denominator+2))*4
            denominator +=2
            first *= -1
        result += a
        return result

print(newtonPi(3))
