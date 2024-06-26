import numpy as np
# 网络时延分为:高、中、低 -> 1, 2, 3
# 响应速度分为:快、中、慢 -> 1, 2, 3
# 流量异常分为:异常、正常、未知 -> 1, 2，3
# 行为异常分为:异常、正常 -> 1, 2
# 存储增大分为:增大、减小、不变 -> 1, 2, 3
# 标签：1:正常， 2:入侵
X = np.array([[1,1,1,2,3],
[2,1,2,1,3],
[3,2,3,2,1],
[1,3,2,2,2],
[2,2,3,2,1],
[3,1,2,1,3],
[1,2,1,2,1],
[2,3,2,1,1],
[2,3,2,1,3],
[2,3,1,2,3],
[3,2,3,1,1]])
# 标签：1:正常， 2:入侵
Y = np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

class My_Module:
    def __init__(self, X, Y):#样本
        self.x = X#属性矩阵
        self.y = Y#类别
        self.all_classes = list(set(Y))#所有类的集合,在本例题中就是{1, 2},为了让其可下标索引，又转换成list,相当于对Y做了一次去重操作
        self.times_classes = []#给出的样本中，每个类出现的频率(概率)
        self.attributes = []#内容是集合，集合装着每个属性可能的取值。

        #开始计算pr_classes
        for c in self.all_classes:
            count = 0
            for item in Y:
                if item == c:
                    count += 1
            self.times_classes.append(count)

        #开始计算attributes
        row, column = X.shape
        for index in range(0, column):
            possible_value = set(X[:, index])
            self.attributes.append(possible_value)






    def predict(self, vector):#给一个属性向量,预测其概率
        result = []
        for i in range(0, len(self.all_classes)):#对每一个类都求概率
            cls = self.all_classes[i]#当前算的是哪个类的概率

            fr_cls = self.times_classes[i]#当前类出现的频率
            buf = fr_cls / len(self.y)#P(c)
            frequency = [0] * len(vector) # 每个元素都是 样本中 类=cls 且 属性与vector相同 出现的频率,即 数学表达式中的|Dc,Xi|
            for j in range(0, len(self.y)):
                if self.y[j] == cls:
                    sample = self.x[j]
                    for k in range(0, len(sample)):
                        if sample[k] == vector[k]:
                            frequency[k] += 1

            #现在对frequency处理，得到p(xi|c)们,并与buf相乘
            for i in range(0, len(frequency)):
                num = frequency[i] + 1#分子
                den = fr_cls + len(self.attributes[i])#分母
                pr = num / den
                buf *= pr

            result.append('为%d类的未归一化概率是%lf'%(cls, buf))
        print(result)


if __name__ == '__main__':
    NB = My_Module(X,Y)
    NB.predict([2,3,1,2,3])
    NB.predict([1,1,2,1,3])



