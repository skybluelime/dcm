import shutil
import os
folder_path = r"I:\부엉이\독수리"
folder_list = os.listdir(folder_path)

target_path = r"I:\부엉이"

def file_to_move_trg_path(trg_path, fpath):
    for x in os.listdir(fpath):
        trg_file = os.path.join(fpath, x)
        if os.path.isfile(trg_file):
            yield trg_file
        elif os.path.isdir(trg_file):
            yield from file_to_move_trg_path(trg_path, trg_file)
        else:
            return

for x in list(file_to_move_trg_path(target_path, folder_path)):
    shutil.move(x, target_path)

