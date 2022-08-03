from tokenize import Double


n = int(input())
a = n
sum = 0
while a >= 10:
    m = n % 10
    n = n//10
    sum += m
    if n < 1 :
        a = sum
        if a > 10 :
            n = a
            sum = 0
    
print(a)
