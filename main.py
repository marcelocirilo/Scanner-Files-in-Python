import os


root = input("Enter the path? ")


filesname=[]
for path, subdirs, files in os.walk(root):
    for name in files:
        filesname.append((os.path.join(path, name)))

print('Total Files: ',len(filesname))

with open('listfiles.txt', 'w') as f:
    for filesname in filesname:
        f.write(f"{filesname}\n")
