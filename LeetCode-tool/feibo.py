# 此题使用动态规划方法求解，自下而上
def feibo(n):
    # 定义一标记数组用来记录已计算过的值，并初始化
    # 之所以要初始化前三位的值，是为了方便计算
    meno = [1, 1, -1]
    # 遍历计算n次
    for index in range(n):
        next_num = sum(meno[-3:])
        meno.append(next_num)
    print(meno[-4:])


if __name__ == "__main__":
    n = 11
    feibo(n)
