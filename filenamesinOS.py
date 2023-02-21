#os walk
import os
path = "D:/KOENIG/koenig-python courses/Advanced python programming"
path1 = os.getcwd()
for (root,dirs,files) in os.walk(path1, topdown=True):
    print(root)
    print(dirs)
    print(files)
    print("***")