import glob
from os import getcwd

dir_path = getcwd()

for files in glob.glob1(dir_path, '*.txt'):
    print(files)

