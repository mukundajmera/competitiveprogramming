import os

def make_folder(folder_name):
    #change file path
    os.chdir(os.path.join(os.getcwd(), folder_name))
    print('working directory is', os.getcwd())
    #read input file and create empty pyhton file for each
    with open('../input.txt', 'r',encoding='utf-8') as file:
        for i in file.read().splitlines():
            os.makedirs(i)
            # file_obj = open(i+'.py', 'a')
            # file_obj.close()


if __name__ == '__main__':
    #set folder name
    folder_name = 'Very Hard'
    make_folder(folder_name)
