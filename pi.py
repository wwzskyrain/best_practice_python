# -*- coding: utf-8 -*-
# 定义一个方法来计算圆的面积
def find_area(r):
    PI = 3.142
    return PI * (r * r)


if __name__ == '__main__':
    print("圆的面积为 %.6f" % find_area(5))
    print(__name__)
