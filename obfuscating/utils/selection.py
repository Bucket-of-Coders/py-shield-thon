import os, time

def filter(path='', enviroment='', master_folder=''):
    in_list = []
    out_list = []
    file_name = []
    dirsa = []
    for root, dirs, files in os.walk(path):
        for fl in files:
            ind = 0
            sub_fol = len(master_folder)

            while True:
                if os.path.join(root, fl)[ind:sub_fol+ind] != master_folder:
                    ind += 1
                else:
                    break

            if fl.endswith('.py'):
                if enviroment != '':
                    if enviroment in root[ind:]:
                        continue

                in_list.append(os.path.join(root, fl).replace('\\', '/'))
                out_list.append(os.path.join(root[ind:], fl).replace('\\', '/'))
                file_name.append(fl)
                for d in dirs:
                    dirsa.append(d)

    file_list = [in_list, out_list, ind+sub_fol, file_name, dirsa]
    return file_list

# if __name__ == '__main__':
#     print(filter(path='C:/test/New folder/111', master_folder='111')[3])
