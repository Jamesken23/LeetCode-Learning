import math
class Solution(object):
    # 进栈出栈顺序计算
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for tok in tokens:
            if tok in ["+", "-", "*", "/"]:
                right_num = stack.pop()
                left_num = stack.pop()
                expression = left_num + tok + right_num
                # 逆波兰表示法进行除法运算时是只保留整数位，既不是向上整数也不是向下整除
                if tok == "/":
                    res = math.trunc(eval(expression))
                else:
                    res = eval(expression)
                stack.append(str(res))
            else:
                stack.append(tok)
        return int(stack.pop())


if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = Solution().evalRPN(tokens)
    print(result)
