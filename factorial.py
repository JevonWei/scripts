def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

number = int(input('Please input a number: '))
result = factorial(number)
print ("%d的阶乘是：%d" % (number,result))
