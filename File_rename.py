import os
directory_path=input("Enter the path:") # Asks User to enter the path
os.chdir(directory_path)
print(os.getcwd())   #display current directory
for file in os.listdir():
    #print(file)
    file_name,file_extension=os.path.splitext(file)
    #print(file_name)
    f1,f2,f3,f4=file_name.split('-')
    f4=f4.zfill(2)
    new_name='{}-{}{}'.format(f4,f1,file_extension)
    os.rename(file,new_name)