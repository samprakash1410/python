import os

def current_directory():
    cwd=os.getpwd()
    print(cwd)
def file_pathname(filename):
    path=os.path.abspath((filename))
    print(path)
    
current_directory 
filename="os.txt"
file_pathname(filename)