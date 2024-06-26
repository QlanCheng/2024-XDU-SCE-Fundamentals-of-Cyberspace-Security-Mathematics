
#欧几里得算法

def EEA(r0, r1):#eea算法，把r_i表示成r0和r1的线性组合
    s = [1, 0]#r0的系数
    t = [0, 1]#r1的系数
    q = []#商
    r = [r0, r1]#余数
    i = 1
    while True:
        i += 1
        r_i = r[i-2] % r[i-1]
        r.append(r_i)#余数
        q.append(r[i-2] // r[i-1])#商

        s_i = s[i-2] - q[i-2] * s[i-1]
        t_i = t[i-2] - q[i-2] * t[i-1]
        s.append(s_i)
        t.append(t_i)

        if r_i == 0:
            print('r: ', r)
            print('s: ', s)
            print('t: ', t)
            print('q: ', q)
            return ['gcd:', r[i-1], 'r0系数:', s[i-1], 'r1系数:', t[i-1]]




def decomposition(number):
    import prime
    print('%d = ' % (number,), end='')
    buf = []
    while number > 1:
        flag = 0#标志
        for p in prime.prime_numbers:
            if number % p == 0:
                buf.append(p)
                number = number / p
                flag = 1
                break

        if not flag:#说明遍历完了质数表，也没有找到一个p可供分解，说明此时质数表已经不够用了
            print('failed')
            exit(1)


    buf.sort()
    rst = []
    count = 1
    for i in range(1, len(buf)):
        if buf[i] == buf[i-1]:
            count += 1
            if i == len(buf) - 1:
                rst.append([buf[i], count])
        else:
            temp = [buf[i-1], count]
            rst.append(temp)
            count = 1
            if i == len(buf) - 1:
                rst.append([buf[i], count])


    for i in range(0, len(rst)):
        if i == len(rst) - 1:
            print(' %d^%d' % tuple(rst[i]), end='')
        else:
            print(' %d^%d *' % tuple(rst[i]), end='')






