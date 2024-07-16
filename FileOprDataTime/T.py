import glob
import os

from khayyam import JalaliDate

# استخراج لیستی از فایل های موجود در فولدر جاری
files_list = glob.glob('*')

extensions_set = set()

# جدا کردن پسوند هر فایل و افزودن آن به ست
for each_file in files_list:
    try:
        extension = each_file.split('.')[1]
        extensions_set.add(extension)
    except:
        continue


# ساخت فولدر بر اساس هر پسوند
def create_folders():
    for ext in extensions_set:
        if ext == 'py':
            continue
        try:
            #باید از strftime استفاده شود که کاراکتر های خاص را پشتیبانی کند
            today = JalaliDate.today().strftime('%A %d %B %Y')
            os.makedirs(today + "/" + ext + '_files')
        except:
            continue


# انتقال فایل ها به دایرکتوری مربوطه
def move_files():
    for each_file in files_list:
        try:
            today = JalaliDate.today().strftime('%A %d %B %Y')
            extension = each_file.split('.')[1]
            if each_file == 'py':
                continue
            elif each_file == "":
                break
            os.rename(each_file, today + "/" + extension + '_files/' + each_file)
        except:
            continue


create_folders()
move_files()
