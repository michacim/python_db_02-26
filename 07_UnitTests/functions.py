

def sum(a, b):
    return a + b

def max1(a,b):
    if a > b:
        return a
    else:
        return b
def max2(li:list)->int:
    if not li:
        raise ValueError("List must not be empty")
    max_value = li[0]
    for i in range(1,len(li)):
        if li[i] > max_value:
            max_value = li[i]

    return max_value

def div1(a,b):
    if b==0:
        raise ZeroDivisionError # besser ValueError
    return a / b


