row = int(input())
col = (2*row) - 1

n = 1
m = 1

for i in range(2,col + 1) :
    while n <= i :
        while m <= (2*i) - 1:
            if m >= row - (n-1) and m <= row + (n-1)  :
                print("*", end = "")
            else :
                print(" ", end ="")
            m += 1
        n += 1
        print("")
        m = 1
    n = 1
    m = 1
   