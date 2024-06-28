import hashlib
import random
import csv

def func(Length, HashValue):
    random.seed(HashValue)
    return random.randint(0, Length-1)




class Bloom:
    def __init__(self, length_of_bloom):
        self.vector = []
        self.length = length_of_bloom
        self.hash_algorithm_list = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b']
        for i in range(0, length_of_bloom):
            self.vector.append(0)

    def set_value_with_certain_hash_algorithm(self, csv_filename, algorithm):
        csvfile = open(csv_filename, mode='r')
        lines = csv.reader(csvfile)

        for line in lines:
            url, isMalicious = line
            if isMalicious == '-1':
                Hash = hashlib.new(name=algorithm, data=url.encode(encoding='utf-8'))
                HashValue = Hash.hexdigest()
                index = func(Length=self.length, HashValue=HashValue)
                self.vector[index] = 1


    def set_value(self, csv_filename):
        for algorithm in self.hash_algorithm_list:
            self.set_value_with_certain_hash_algorithm(csv_filename=csv_filename, algorithm=algorithm)



    def verify(self,csv_filename):
        harmless_counter = 0#无害的总数
        harmful_counter = 0#有害的总数
        error_in_harmless = 0#无害的却过滤了的数量
        error_in_harmful = 0#有害但没过滤的数量


        csvfile = open(csv_filename, mode='r')
        lines = csv.reader(csvfile)

        for line in lines:
            url, isMalicious = line
            if isMalicious == '1':#无害
                harmless_counter += 1
                if self.filter(url) == 1:
                    error_in_harmless += 1
            elif isMalicious == '-1':#有害
                harmful_counter += 1
                if self.filter(url) == 0:
                    error_in_harmful += 1

        print('无害总数:', harmless_counter, ' 发生错误数:', error_in_harmless, '错误率:', error_in_harmless / harmless_counter)
        print('有害总数:', harmful_counter, ' 发生错误数:', error_in_harmful, '错误率:', error_in_harmful / harmful_counter)



    def filter(self, url):#接受一个url，返回0代表通过，1代表拦截
        for name in self.hash_algorithm_list:
            Hash = hashlib.new(name=name, data=url.encode(encoding='utf-8'))
            HashValue = Hash.hexdigest()
            index = func(Length=self.length, HashValue=HashValue)
            if self.vector[index] == 0:
                return 0
        return 1



if __name__ == '__main__':
    filename = 'dataset.csv'
    length = 97065
    B = Bloom(length_of_bloom=length)
    B.set_value(csv_filename=filename)
    print('length = ', length)
    print('Hash函数个数(k) = ', len(B.hash_algorithm_list))
    B.verify(csv_filename=filename)

