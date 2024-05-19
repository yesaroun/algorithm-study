
# 안녕하십니까 교수님
# 제가 맥os여서 python이 저장된 경로를 찾아보니 아래와 같았습니다.
# 그리고 해당 폴더의 모든 하위 디렉터리를 재귀함수를 이용해서 구현해보았으나
# 실행되는데 시간이 조금 걸립니다.ㅜㅜ

import os

class Recursive_dirfile:
    def __init__(self, dir_names):
        self.dir_names = dir_names
    
    def recursive_dirfile(self, new_path):
        path = new_path
        dirfiles = os.listdir(path)

        for each in dirfiles:
            full_name = path + each + "/"
            if os.path.isdir(full_name):
                # print(full_name)
                self.dir_names.append(full_name)
                # print(dir_names)
                Recursive_dirfile.recursive_dirfile(self, full_name)


if __name__ == "__main__":
    path = "/Users/akor1/opt/anaconda3/"
    dir_names = []
    
    re1 = Recursive_dirfile(dir_names)
    re1.recursive_dirfile(path)
    print(re1.dir_names)
