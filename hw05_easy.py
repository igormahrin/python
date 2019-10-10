import os,sys,shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def createfolder():
    for d in  range(1,10):
        path = "dir_"+str(d)
        os.mkdir(path)

def deletefolder():
    for d in  range(1,10):
        path = "dir_"+str(d)
        os.rmdir(path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
content = os.listdir(path=".")
print(content)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
shutil.copy('hw05_easy.py', 'my_copy')