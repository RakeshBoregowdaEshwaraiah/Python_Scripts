import os
directory_path=input("Enter the path:") # Demanding for path where you need to replace files
os.chdir(directory_path) # changing directory to user's input
print(os.getcwd())   #display current directory
for file in os.listdir():
    #print(file)  # output all contents of directory
    file_name,file_extension=os.path.splitext(file) # splitting extension and name of the file
    #print(file_name)
    f1,f2,f3,f4=file_name.split('-') # you can choose variables depending on the name of file given
    f4=f4.zfill(2) # example 00 file, 01 file1, 02 file2
    new_name='{}-{}{}'.format(f4,f1,file_extension)
    os.rename(file,new_name)
