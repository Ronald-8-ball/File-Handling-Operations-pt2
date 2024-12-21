with open('file.txt','w') as f:
    f.write("I conqured this line")
f.close()

with open('file.txt','r') as f:
    f.readlines()
    for x in f:
        data = x.split()
        print(data)
f.close()

import os
path = '/home/User/Desktop/File.txt'
file = os.path.isfile(path) 
print(file) 

os.remove('Invader.txt')