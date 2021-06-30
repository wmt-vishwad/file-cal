import os

root =  "C:\pycharm project\project1"
from collections import Counter
counts = Counter()
for c_dir, dirname, filenames in os.walk('.'):
    for filename in filenames:
        before_ext, extension = os.path.splitext(filename)
        counts[extension] += 1
        for extension, count in counts.items():
            print(f"{extension:8}{count}")
def list_all(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(file):
            list_all(file)
        else:
            print("\t", files)
cpt = sum([len(files) for r,d, files in os.walk("C:\pycharm project\project1")])

list_all(root)