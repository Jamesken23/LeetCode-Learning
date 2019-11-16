class Solution(object):
    # 本题采用广度遍历方法
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 首先给wordList列表中单词去重
        word_set = set(wordList)
        word_dict = {}
        for word in word_set:
            for index in range(len(word)):
                new_word = word[:index]+"_"+word[index+1:]
                if new_word not in word_dict.keys():
                    word_dict[new_word] = [word]
                else:
                    word_dict[new_word].append(word)
        print("word_dict", word_dict)
        # 定义当前层的单词集合为beginWord
        cur_word = [beginWord]
        # 定义下一层的单词集合
        next_word = []
        # 定义从 beginWord 到 endWord 的最短转换序列的长度
        depth = 1
        while cur_word:
            for word in cur_word:
                # 如果endWord出现在当前层的cur_word单词集合中，则立即返回该深度
                if word == endWord:
                    return depth
                for index in range(len(word)):
                    new_word = word[:index]+"_"+word[index+1:]
                    if new_word in word_dict.keys():
                        for w in word_dict[new_word]:
                            if w not in next_word:
                                next_word.append(w)
                        del word_dict[new_word]
            # 如果endWord未出现在当前层的cur_word单词集合中，则深度+1
            depth += 1
            cur_word = next_word
            next_word = []
        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sequence_length = Solution().ladderLength(beginWord, endWord, wordList)
    print(sequence_length)
