import numpy as np
import copy

def multiply(number, item):#这个函数旨在对列表进行数乘，例如multiply(2, [[1,2], [3,4]]),希望返回一个[[2,4], [6,8]]
    spam = copy.deepcopy(item)#进行这种操作的时候不希望是原地修改的，否则会引起意想不到的错误
    if isinstance(spam, list):
        for index in range(0, len(spam)):
            spam[index] = multiply(number, spam[index])
    else:
        return number * spam
    return spam

def index_of_max(array):
    rst = 0
    for i in range(0, len(array)):
        if array[i] >= array[rst]:
            rst = i
    return rst


class HMM:
    def __init__(self, A, B, P=None):
        self.A = np.array(A)
        self.B = np.array(B)
        self.P = np.array(P)
    #A： 一步转移矩阵 B：发射矩阵  P：概率向量，可以暂时不给出

    def exhaustion_observation_sequence(self, length, p='default' ):#给出一个初始的概率向量p，穷举其可能的观测序列及其概率,length为长度
        if p == 'default':
            p = self.P
        p = np.array(p).T
        rst = []
        probability_wide, probability_narrow = self.B.dot(p)  # 初始时刻观测到宽、窄的概率
        rst.append(probability_wide)
        rst.append(probability_narrow)

        for cnt in range(1, length):
            p = self.A.dot(p) #更新概率向量
            probability_wide, probability_narrow = self.B.dot(p)  # 这一时刻观测到宽、窄的概率
            buf1 = multiply(probability_wide, rst)
            buf2 = multiply(probability_narrow, rst)
            rst = [buf1, buf2]
        return rst

    def probability_of_certain_array(self, string, p='default'):
        if p == 'default':
            p = self.P
        p = np.array(p).T
        probability = 1
        for i in string:
            spam = self.B.dot(p)
            buf = spam[0] if i == '宽' else spam[1]
            probability *= buf
            p = self.A.dot(p)
        return probability

    def exhaustion_hidden_sequence(self, length, p='default'):
        if p == 'default':
            p = self.P
        p = np.array(p).T
        zero, one, nothing = self.A.dot(p)
        rst = [zero, one, nothing]
        for cnt in range(1, length):
            p = self.A.dot(p) #更新概率向量
            zero, one, nothing = self.A.dot(p)  # 这一时刻0\1\无的概率
            buf1 = multiply(zero, rst)
            buf2 = multiply(one, rst)
            buf3 = multiply(nothing, rst)
            rst = [buf1, buf2, buf3]
        return rst

    def HiddenSequence_Cause_ObservationSequence(self, HS, OS):#HS、OS为形如[0, 1, 2]或“宽窄宽”这样的任何可下标索引的数据结构
        probability = 1
        for cnt in range(0, len(HS)):
            i = 0 if OS[cnt] == '宽' else 1
            j = HS[cnt] #B矩阵的行、列下标
            probability *= self.B[i][j]
        return probability





    def most_probable_hidden_sequence(self, sequence):#sequence为观测序列
        I_list = self.exhaustion_hidden_sequence(length=len(sequence))#所有I的·概率
        result = []
        self.func(I_list=I_list, HS=[], OS=sequence, result=result)
        result.sort(key=lambda item: item[1], reverse=True)
        return result





    def func(self, I_list, HS, OS, result):
        for i in range(0, len(I_list)):
            HS.append(i)#记录下当前进入的下标
            if type(I_list[i]) == type(I_list):
                self.func(I_list[i], HS=HS, OS=OS, result=result)
                HS.pop()#HS就像一个栈，记录了下标，完成访问操作之后弹出
            else:
                probability = self.HiddenSequence_Cause_ObservationSequence(HS=HS, OS=OS)
                #已经访问到嵌套的最底层了，开始计算当前 隐藏序列 产生给定 观测序列 的概率
                result.append([HS[:], probability * I_list[i]])  #probability = P(O|I) ; I_list[i] = P(I)
                HS.pop()

        return result

    def Viterbi(self, Observation_Sequence, p='default'):
        #接受一个观测序列OS和一个初始概率向量P，如果P不给出，默认用self.P计算，但可能会改变self.P的值
        #返回为一个形如[0, 1, 2]的列表，代表最可能的隐藏序列
        if p == 'default':
            p = self.P
        p = np.array(p).T
        result = []

        for o in Observation_Sequence:
            p = self.A.dot(p)#如果p取稳态分布的p，这里应该不会改变p的值
            buf = []
            index2 = 0 if o == '宽' else 1

            for index1 in range(0, len(p)):
                buf.append(p[index1] * self.B[index2][index1])

            state = index_of_max(buf)#此时确定的状态
            result.append(state)
            p = [0, 0, 0]
            p[state] = 1
            p = np.array(p).T

        return result


if __name__ == '__main__':
    A = [[0.5, 0, 0.4], [0.2, 0.7, 0.2], [0.3, 0.3, 0.4]]
    B = [[0.9, 0.8, 0.6], [0.1, 0.2, 0.4]]
    hmm = HMM(A, B, P=[0.26666667, 0.4, 0.33333333])
    sequence = ('宽', '窄', '宽')
    rst = hmm.HiddenSequence_Cause_ObservationSequence(HS=[1, 2, 1], OS=sequence)
    print(rst)
