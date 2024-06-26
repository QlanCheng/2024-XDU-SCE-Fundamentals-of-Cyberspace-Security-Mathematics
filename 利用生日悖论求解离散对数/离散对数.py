import random

def attack(y, g, p):
    while True:
        A = Create_Table_A(g=g, p=p)
        B = Create_Table_B(y=y, g=g, p=p)
        for i in A.keys():
            if i in B:#如果B的keys里面有i
                a, b = A[i], B[i]
                x = (a-b) % (p-1)
                print('x =', x)
                return None
            print(i)
        print('失败一次')



def Create_Table_A(g, p):
    A = dict()
    for counter in range(0, int(p**0.5)):
        a = random.randint(0, p-1)
        ga = (g**a) % p
        A[ga] = a#键是ga,值是a,方便查询
        print(counter)
    return A #用字典是因为字典是底层是用哈希表实现的，查找速度非常快。



def Create_Table_B(y, g, p):
    B = dict()
    for counter in range(0, int(p**0.5)):
        b = random.randint(0, p-1)
        gb = (g**b) % p
        ygb = (y * gb) % p
        B[ygb] = b
        print(counter)
    return B


if __name__ == '__main__':
    y = 5125495
    g = 3
    p = 5767169

    attack(y, g, p)