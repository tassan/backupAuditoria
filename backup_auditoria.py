from os import walk
from os import getcwd

#dir_path = getcwd()

dir_path =

for root, dirs, files in walk(dir_path):
    for file in files:
        if file.endswith(".txt"):
            print(file)
