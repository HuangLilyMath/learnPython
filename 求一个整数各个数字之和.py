def sumDigits(n):
    b = len(str(n))
    c = int(n)
    s = 0
    for i in range(1,b+1):
        d = c % 10
        s = s + d
        c = c // 10
    print(s)

n = input()
sumDigits(n)







