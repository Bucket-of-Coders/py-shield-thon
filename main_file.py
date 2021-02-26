import sys
sys.dont_write_bytecode = True
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import os, pickle
import binascii, zlib, time
import shutil
import time,base64

# local library
from sydsec.obfuscating.feature import press, hexing, compression, adding_password
from secure import encode, encrypt

def file_protect(inp='', out=''):
    if os.path.exists(out+'/sydeco_secure/'):
        pass
    else:
        os.makedirs(out+'/sydeco_secure/')
    try:
        c = 1
        for num,data in enumerate(inp):
          if '/' not in inp[-c:]:
            c+=1
          else:
            c-=1;break
        files_n = inp[-c:]
        outs = out+'/sydeco_secure/'
        adding_password.files(inp, outs+files_n)
        press.main(outs+files_n, outs+files_n[:-3]+'_.py')
        encode.main(outs+files_n[:-3]+'_.py', outs+files_n[:-3]+'_bak.py')
        hexing.main(outs+files_n[:-3]+'_bak.py', outs+files_n[:-3]+'_1.py')
        encrypt.main(outs+files_n[:-3]+'_1.py',outs+files_n[:-3]+'_1bak.py')
        compression.compress(outs+files_n[:-3]+'_1bak.py', outs+files_n[:-3]+'_com.py')
        encrypt.main(outs+files_n[:-3]+'_com.py', outs+files_n[:-3]+'_.py')
        encrypt.main(outs+files_n[:-3]+'_.py',outs+files_n)

        if not os.path.exists(outs+'basedir_sydeco.py'):
            with open(outs+'basedir_sydeco.py', 'w') as dir:
                dir.write('import os\nabs_p=os.path.dirname(os.path.realpath(__file__))')
                dir.close()
    except Exception as e:
        print(e)
        print('[-] Something went wrong please try again')
        sys.exit(1)

# if __name__ == '__main__':
#     file_protect(r'F:\sydsec\folder\turtle_test.py', r'D:\test\1')
