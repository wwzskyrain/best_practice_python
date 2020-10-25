# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 九九乘法表
def print_nine_multi_nine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()


if __name__ == '__main__':
    print_nine_multi_nine()


