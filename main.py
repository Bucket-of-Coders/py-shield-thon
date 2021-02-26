import sys
sys.dont_write_bytecode = True
from sydsec.obfuscating.feature import press, hexing, compression, adding_password
from sydsec.obfuscating.utils import selection,directory
from secure import encode, encrypt
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import os, pickle
import binascii, zlib, time
import shutil
import time,base64

def create(path='', enviroment='', master_folder=''):

    full_master = selection.filter(path=path.replace('\\', '/'), enviroment=enviroment, # getting the indentation slicing
    master_folder=master_folder)[2]                                                     # for gettin the absolute path

    try:
        if os.path.exists(path[:full_master]+'/sydeco_secure/'):
            shutil.rmtree(path[:full_master]+'/sydeco_secure/')
            time.sleep(2)
    except:
        print('[!]   The folder is being open!!\n[!]   Please close the application that use the project folder and try again')
        sys.exit(1)

    inp = selection.filter(path=path.replace('\\', '/'), enviroment=enviroment,
                           master_folder=master_folder)[0]
    out = selection.filter(path=path.replace('\\', '/'), enviroment=enviroment,
                           master_folder=master_folder)[1]
    file_name = selection.filter(path=path.replace('\\', '/'), enviroment=enviroment,
                                 master_folder=master_folder)[3]
    dr = selection.filter(path=path.replace('\\', '/'), enviroment=enviroment,
                                 master_folder=master_folder)[4]



    print('Begining protect your code with sydeco secure\n')

    for ind, items in enumerate(inp):
        time.sleep(.5)
        for x,y in enumerate(file_name):
            if not os.path.exists(path[:full_master]+'/sydeco_secure/'+out[x][:-len(y)-1]):
                os.makedirs(path[:full_master]+'/sydeco_secure/'+out[x][:-len(y)-1])

        #generate the password
        # pas = []
        # gen_password = adding_password.gen_password().gen_data() # output is 32 alphanumeric and symbol
        # dir_img = directory.get_dir().directory()
        # image = text_image.encode_text(get_image(), base64.b64encode(gen_password), dir_img)
        # gen_password_base64 = base64.b64encode(gen_password) # encode the password using b64encode and input into image
        # for x in range(3):
        #     pas.append([directory.get_dir().directory(),
        #                 gen_password,
        #                 get_image()]) # output will directory and name of output image
        # print(pas)
        # for c in range(3):
        #     image = text_image.encode_text(pas[c][2], base64.b64encode(pas[c][1]), pas[c][0])


        # data = open(random_image, 'wb') #starting write for Input
        # pickle.dump(gen_password_base64, data)
        # data.close()

        #executing the secure file
        try:
            out_file = path[:full_master]+'/sydeco_secure/'+out[ind]
            print('File : {}\nFile number : {}\n'.format(out[ind], ind+1))
            adding_password.files(items, items[:-3]+'__12.py') #can import but cannot calling the object
            print('\n[+] Compressing yor code')
            press.main(items[:-3]+'__12.py', out_file)
            print('[+] encoding and converting your code')
            encode.main(out_file, out_file[:-3]+'_1.py')
            hexing.main(out_file[:-3]+'_1.py', out_file, level='high')
            encrypt.main(out_file, items[:-3]+'_comp.py')
            print('[+] HEXING your code')
            compression.compress(items[:-3]+'_comp.py', out_file[:-3]+'_bak.py')
            print('[+] Finalisation\n\n')
            encrypt.main(out_file[:-3]+'_bak.py', out_file[:-3]+'_bak1.py')
            encrypt.main(out_file[:-3]+'_bak1.py', out_file)
            xx = 1
            for num,das in enumerate(out[ind]):
                if not '/' in out[ind][-xx:]:
                    xx+=1
                else:
                    print(out[ind][:-xx])
                    break
            #py_compile
            #os system run :
            #   - activate python3 and run the disasamble.py
            #   - inside disasamble.py os system rum xdis > file.pyasm
            #   - open file.pyasm if the file.read() has opcode
            #   - change it into number out of index
            #   - and os system run xasm py_compile
            #   - done
        except Exception as e:
            print(e)
            print('[-] Something went wrong please try again')
            sys.exit(1)

        # file = out_file
        # os.chmod(file, S_IREAD)

    if not os.path.isfile(path[:full_master]+'/sydeco_secure/'+master_folder+'/basedir_sydeco.py'):
        with open(path[:full_master]+'/sydeco_secure/'+master_folder+'/basedir_sydeco.py', 'w') as dir:
            dir.write('import os\nabs_p=os.path.dirname(os.path.realpath(__file__))')
            dir.close()

    # with open('import_.py', 'w') as f:
    #     f.write("""import httpimport
    #     httpimport.logger.disabled = True
    #     httpimport.INSECURE = True
    #     with httpimport.remote_repo(['turtle_test', 'extract', 'basedir_sydeco', 'im2'], ip):
    #         with httpimport.remote_repo(['iml'], ip+'/im2'):
    #             import basedir_sydeco
    #             import extract
    #             import turtle_test
    #             import iml
    #     turtle_test.main()
    #     turtle_test.mainloop()
    #     iml.codes('to code')""")

    print('\n[+] Finish')

# create(path=r'F:\sydsec\folder\sydsec', master_folder='sydsec')
