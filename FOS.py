import os
from datetime import datetime
print(os.getcwd())
#os.rename('File.txt','Test.txt')
time=os.stat('Test.txt').st_mtime
print(datetime.fromtimestamp(time))
for dirpath,dirnames,filenames in os.walk(os.getcwd()):
    print("Dirpath=",dirpath)
    print("Dirname=",dirnames)
    print("Filename=",filenames)
print(os.listdir())
print(os.path.basename('E:\Python\Test.txt'))
print(os.path.dirname('E:\Python\Test.txt'))
print(os.path.exists('E:\Python\Test.txt'))
print(os.path.isfile('E:\Python\Test.txt'))
print(os.path.isdir('E:\Python'))

if(os.path.exists('E:\Python')):
    with open('E:\Python\Demo.txt','w') as f:
        f.write('They are taking the hobbits to Isengard')

print(os.listdir())