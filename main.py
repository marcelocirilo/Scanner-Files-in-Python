import os


root = input("Enter the path? ")



totalfiles=0
filesname=[]
for path, subdirs, files in os.walk(root):
    for name in files:
        filesname.append((os.path.join(path, name)))

print('Total Arquivos: ',len(filesname))

with open('listfiles.txt', 'w') as f:
    for filesname in filesname:
        f.write(f"{filesname}\n")