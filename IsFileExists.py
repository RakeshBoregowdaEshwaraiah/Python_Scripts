import os

# Path IN which we have to search file
PATH = input("Enter the path where you want to check for file")   

def searchFile(fileName):
    ''' This function searches for the specified file name in the given PATH '''
    for root, dirs, files in os.walk(PATH):
        print('Looking in:',root)
        for Files in files:
            try:
                found = Files.find(fileName)        # Returns -1 if NOT found else returns index
                # print(found)
                if found != -1:
                    print(fileName, 'Found')
                    break
            except:
                exit()

if __name__ == '__main__':
    searchFile('new_file.txt')  
    #searchingfile
