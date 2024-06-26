import math
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


def cal_entropy(l):
    sum = 0
    entropy = 0
    for i in l:
        sum += i

    for i in l:
        pr = i / sum
        entropy += -1 * pr * math.log2(pr)
    return entropy

#决策树也是树，这是树的节点类
class Node:
    def __init__(self, set_of_index=None, set_of_counter=None, entropy=None):
        self.set_of_index = set_of_index
        self.set_of_counter = set_of_counter
        self.entropy = entropy
        self.child = None
        self.division_choice = None

    def __str__(self):
        return str(self.set_of_index) + '  ' + str(self.set_of_counter) + '  ' + str(self.entropy)

    def display(self):
        print(self,end='  ')
        print('分割方案', self.division_choice)
        if self.child:
            for i in range(0, len(self.child)):
                print('第', i, '个子集', self.child[i])
            print()
            for child in self.child:
                child.display()




class My_Module:
    def __init__(self, X, Y):#样本
        self.X = X#属性矩阵
        self.Y = list(Y)
        self.class_names = list(set(Y))#所有类的集合,在本例题中就是{1, 2},为了让其可下标索引，又转换成list,相当于对Y做了一次去重操作
        self.features = []#内容是集合，集合装着每个属性可能的取值。
        self.DecisionTree = None
        #开始计算features
        row, column = X.shape
        for index in range(0, column):
            possible_value = set(X[:, index])
            self.features.append(possible_value)

        #开始计算entropy
        buf = []
        for cls in self.class_names:
            frequency = self.Y.count(cls)
            buf.append(frequency)
        self.entropy = cal_entropy(buf)

    def classify(self, feature, node):#对样本集合（或子集）分一次类,feature下标是Index
        index = feature
        possible_value = list(self.features[index])
        subsets = []
        #开始计算子集
        #子集做初始化
        for i in range(0, len(possible_value)):
            buf = []
            subsets.append(buf)
        #subsets就会长这样:[[],[],[]]
        #下面开始遍历一次样本，按属性分类。
        for i in node.set_of_index:
            sample = self.X[i]
            index1 = possible_value.index(sample[index])
            subsets[index1].append(i)

        #print('按下标为:', index, '的属性分类，共分为', len(possible_value), '个子集', '含有不同类的样本个数分别为',subsets)

        return subsets

    def create_node(self, set_of_index):#由下标的集合 算出节点所需的信息
        if not set_of_index:
            return None
        buf = [self.Y[index] for index in set_of_index]
        diversity = list(set(buf))
        set_of_counter = [0] * len(diversity)
        for cls in buf:
            index = diversity.index(cls)
            set_of_counter[index] += 1

        entropy = cal_entropy(set_of_counter)

        return Node(set_of_index, set_of_counter, entropy)

    def decide(self, node):#对一个决策树节点，进行下一步决策,决定以什么feature为分类
        if node.entropy == 0:
            return -1

        container = []#装各个分类下的节点
        #开始计算所有决策
        for feature_index in range(0, len(self.features)):
            subsets = self.classify(feature=feature_index,node=node)
            buf = []
            for set_of_index in subsets:
                nd = self.create_node(set_of_index=set_of_index)
                if nd:
                    buf.append(nd)
            container.append(buf)

        #开始分析每个决策导致的信息增量，比较之
        gains = []
        card = len(node.set_of_index)
        for division in container:
            new_entropy = 0
            for n in division:#n是node对象
                n_card = len(n.set_of_index)
                new_entropy += (n_card/card) * n.entropy
            #print('________________________________________________')
            gains.append(node.entropy - new_entropy)

        max_gain = max(gains)
        choice = gains.index(max_gain)
        #print(gains)
        #print('节点', node, '的最佳分类法是按下标为', choice, '的属性分类')

        return choice, container[choice]#返回决策，及其分割

        

    def create_decision_tree(self):
        tree = self.create_node(set_of_index=range(0, len(self.Y)))
        self.divide(node=tree)
        return tree


    def divide(self, node):
        buf = self.decide(node=node)
        if buf == -1:
            return None
        else:
            node.division_choice, node.child = buf
            for child in node.child:
                self.divide(node=child)




if __name__ == '__main__':
    M = My_Module(X, Y)
    tree = M.create_decision_tree()
    tree.display()

