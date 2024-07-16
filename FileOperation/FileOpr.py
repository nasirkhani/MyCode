import glob
import os

files_list = glob.glob('*')

extensions_set = set()

for each_file in files_list:
    try:
        extension = each_file.split('.')[1]
        extensions_set.add(extension)
    except:
        continue


def create_folders():
    for ext in extensions_set:
        if ext == 'py':
            continue
        try:
            os.makedirs(ext + '_files')
        except:
            continue


def move_files():
    for each_file in files_list:
        try:
            extension = each_file.split('.')[1]
            if each_file == 'py':
                continue
            elif each_file == "":
              break
            os.rename(each_file, extension + '_files/' + each_file)
        except:
            continue


create_folders()
move_files()
