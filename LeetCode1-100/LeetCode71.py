class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = list(path)
        start = 0
        while start < len(path_list)-1:
            if path_list[start] == "/":
                if path_list[start+1] == "/":
                    path_list.pop(start)
                else:
                    start += 1
            elif path_list[start] == ".":
                if path_list[start+1] == "/":
                    path_list.pop(start)
                    path_list.pop(start)
                elif path_list[start+1] == ".":
                    start += 2
            else:
                start += 1
        print("path_list", path_list)
        path_str = "".join(path_list).split("/")
        path_str.remove("")
        print("path_str", path_str)
        
        while ".." in path_str:
            index = path_str.index("..")
            if index > 0:
               path_str.pop(index-1)
               path_str.pop(index-1)
            else:
               path_str.pop(index)
        new_path = []
        for index in path_str:
            if index not in ["", "."]:
                new_path.append("/")
                new_path.append(index)
        if len(new_path) == 0:
            return "/"
        else:
            return "".join(new_path)


if __name__ == "__main__":
    path = "/a//b////c/d//././/.."
    new_path = Solution().simplifyPath(path)
    print(new_path)
