class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # 首先将给定的words字符串数组按照最大长度maxWidth分组
        word_group = []
        word_width = 0
        group = []
        for word in words:
            if word_width + len(word) <= maxWidth:
                group.append(word)
                word_width += len(word)+1
            else:
                word_group.append(group[:])
                group = [word]
                word_width = len(word)+1
        if len(group) > 0:
            word_group.append(group)
        # 得到新的分组列表之后，开始对每一组插入空格
        for group_index in range(len(word_group)):
            if group_index < len(word_group)-1:
                group_length = len("".join(word_group[group_index]))
                if len(word_group[group_index]) == 1:
                     word_group[group_index].extend([" "]*(maxWidth-group_length))
                else:
                    indice = (maxWidth-group_length)//(len(word_group[group_index])-1)
                    addition = (maxWidth-group_length)%(len(word_group[group_index])-1)
                    for index in range(len(word_group[group_index])-1):
                        str_list = list(word_group[group_index][index])
                        if index < addition:
                            str_list.extend([" "]*(indice+1))
                        else:
                            str_list.extend([" "]*indice)
                        word_group[group_index][index] = "".join(str_list)
            else:
               group_length = len("".join(word_group[group_index]))
               group_length += len(word_group[group_index]) - 1
               for index in range(len(word_group[group_index])):
                   str_list = list(word_group[group_index][index])
                   if index < len(word_group[group_index]) - 1:
                       str_list.append(" ")
                   else:
                       str_list.extend([" "]*(maxWidth-group_length))
                   word_group[group_index][index] = "".join(str_list)
        new_words = []
        for group in word_group:
            new_words.append("".join(group))
        return new_words


if __name__ == "__main__":
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    new_words = Solution().fullJustify(words, maxWidth)
    print(new_words)
