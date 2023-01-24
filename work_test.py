import shutil
import os
folder_path = r"G:\분류\SSNI"
folder_list = os.listdir(folder_path)

fpath = r"I:\분류\SSNI"


fpath
for fold in folder_list:
    for fname in os.listdir(fpath):
        if fold.upper() in fname.upper():
            print(fname)
            trg_folder = os.path.join(folder_path, fold)
            src_file = os.path.join(fpath, fname)
            shutil.move(src_file, trg_folder)


for fname in folder_list:
    src_file = os.path.join(folder_path, fname)
    print(src_file)
    shutil.move(src_file, fpath)


