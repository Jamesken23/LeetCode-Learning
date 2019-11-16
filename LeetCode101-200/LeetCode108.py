class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 首先将给定字符串以空格符切分
        str_split = str.split()
        str_list = []
        if len(str_split) == 0:
            return 0
        for indice in range(len(str_split)):
            if str_split[indice][0] == '-' and len(str_split[indice]) >= 2:
                str_list.append('-')
                for str_indice in range(1, len(str_split[indice])):
                    if '0' <= str_split[indice][str_indice] <= '9':
                        str_list.append(str_split[indice][str_indice])
                    else:
                        break
                if len(str_list) == 1:
                    return 0
                else:
                    str_copy = int(''.join(str_list))
                    if str_copy <= -2**31:
                        return -2**31
                    if str_copy >= 2**31 - 1:
                        return 2**31 - 1
                    return  str_copy
            elif str_split[indice][0] == '+' and len(str_split[indice]) >= 2:
                for str_indice in range(1, len(str_split[indice])):
                    if '0' <= str_split[indice][str_indice] <= '9':
                        str_list.append(str_split[indice][str_indice])
                    else:
                        break
                if len(str_list) == 0:
                    return 0
                else:
                    str_copy = int(''.join(str_list))
                    if str_copy <= -2 ** 31:
                        return -2 ** 31
                    if str_copy >= 2 ** 31 - 1:
                        return 2 ** 31 - 1
                    return str_copy
            elif '0' <= str_split[indice][0] <= '9':
                for str_indice in range(len(str_split[indice])):
                    if '0' <= str_split[indice][str_indice] <= '9':
                        str_list.append(str_split[indice][str_indice])
                    else:
                        break
                str_copy = int(''.join(str_list))
                if str_copy <= -2 ** 31:
                    return -2 ** 31
                if str_copy >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                return str_copy
            else:
                return 0
            

if __name__ == "__main__":
    init_str = "4.193"
    str_to_int = Solution().myAtoi(init_str)
    print(str_to_int)
