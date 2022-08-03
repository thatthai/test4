row = int(input())


n = 1
m = 1
k = 2

while k <= row + 1 :
    while n <= k :
        while m <= (2*(row+1)) - 1:
            if m >= row+1 - (n-1) and m <= row+1 + (n-1)  :
                print("*", end = "")
            else :
                print(" ", end ="")
            m += 1
        n += 1
        print("")
        m = 1
    n = 1
    m = 1
    k += 1

print(" " * row , end = "")
print("|")
print("=" * row , end = "")
print("V", end = "")
print("=" * row)