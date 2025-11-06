# 4 A)
for i in range(1, 11):
    print(i*i)
#4 B)
for i in [1,3,5,7,9]:
    print(i, ":", i**3)
    print(i)
#4 C)
    x=2
    y = 10
for j in range(0, y, x):
    print(j, end="")
    print(x + y)
    print("done")
#4 D)
    ans = 0
for i in range(1,11):
    ans = ans + i*i
    print("i:", i)
    print("ans:", ans)
    input("Press <Enter> to quit")
