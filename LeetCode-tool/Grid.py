def count_route():
    # 首先初始化一个5x6的方格，其中-10表示障碍物，-5表示可以填充数字
    flag_matrix = [[-10]*6]
    for index in range(3):
        flag_matrix.append([-10, -5, -5, -5, -5, -10])
    flag_matrix.append([[-10]*6])   
    flag_matrix[1][1] = -10
    flag_matrix[3][4] = -10
    # 定义当前点可移动的方向
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 保存结果的集合
    grid_list = []

    # 核心的递归算法
    def back(start=[1,2], count=0):
        if count == 10:
            grid_list.append(flag_matrix[:][:])
            return
        for index in range(10):
            start_x = start[0]
            start_y = start[1]
            if flag_matrix[start_x][start_y] == -5:
                if conflict(start_x, start_y, index, flag_matrix):                    
                    for direc in directions:
                        
                        next_direction = [start_x+direc[0], start_y+direc[1]]
                        if next_direction[0] in range(1, 4) and next_direction[0] in range(1, 5):
                            flag_matrix[start_x][start_y] = index
                            back(next_direction, count+1)
                            flag_matrix[start_x][start_y] = -5

    back()
    return len(grid_list)
                

# 判断当前小方格的点是否与相邻点冲突
def conflict(x, y, value, flag_matrix):
    neighbor_val = []
    relate_value = [value-1, value+1]
    for col in range(x-1, x+2):
        if value-1 in flag_matrix[col][y-1:y+2] or value+1 in flag_matrix[col][y-1:y+2]:
            return False
    return True
    

if __name__ == "__main__":
    count_route()
