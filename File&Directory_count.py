#Script is used to count number of files and directories in a diectory recursively
import os

# Path IN which we have to count files and directories
PATH = 'C:\Users\RAKESBE\Desktop\Personal\Work\Python\scripts'   # Enter your path here

fileCount = 0
Directory_Count= 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:',root)
    for directories in dirs:
        Directory_Count += 1
    for Files in files:
        fileCount += 1

print('Number of files',fileCount)
print('Number of Directories',dirCount)
print('Total:',(dirCount + fileCount))