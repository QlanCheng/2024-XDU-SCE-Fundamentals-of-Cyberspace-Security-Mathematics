class Group:
    def __init__(self, set, modulus):
        self.set = tuple(set)
        self.cardinality = len(set)
        self.modulus = modulus
        self.ords = None
        self.generators = None
        self.calculate_ords()

    def calculate_ords(self, display=False):#计算每个元素的阶，顺便算出生成元们
        result = []
        generator = []
        for number in self.set:
            ord_number = self.ord(number)
            temp = [number, ord_number]
            result.append(temp)
            if ord_number == self.cardinality:#如果阶数等于基数
                generator.append(number)
        if display:
            for i in result:
                print('ord(%d) = %d' % tuple(i))
            print(generator)
        self.ords = result
        self.generators = generator




    def ord(self, number, display=False):#计算某个特定元素的阶
        temp = number
        for exp in range(1, self.modulus):
            if temp == 1:
                if display:
                    print('%d 的%d次方 mod %d = 1' % (number, exp, self.modulus))
                    print('ord(%d) = %d' % (number, exp))
                return exp
            else:
                if display:
                    print('%d 的%d次方 mod %d = %d' % (number, exp, self.modulus, temp))
            temp = (temp * number) % self.modulus

    def child_group(self, k):#k是子群基数
        rst = []
        alpha = self.generators[0]#alpha是母群的一个生成元
        a = (alpha ** (self.cardinality / k)) % self.modulus #a是子群的一个生成元
        a = int(a)
        print('生成元是', a)
        temp = a
        for i in range(0, k):#迭代k次
            rst.append(temp)
            temp = (temp * a) % self.modulus
        rst.sort()
        return rst

if __name__ == '__main__':
    A = []
    for i in range(1, 40961):
        A.append(i)
    GR = Group(set=A, modulus=40961)
    GR.ord(4,True)








