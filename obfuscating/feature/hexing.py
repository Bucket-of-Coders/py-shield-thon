from __future__ import with_statement

import sys
sys.dont_write_bytecode= True
try:
    from obfuscating.utils import mixer_string
    import os
except Exception:
    from sydsec.obfuscating.utils import mixer_string
    import os

def str_hex(files, out, level, extr):

    if type(files) is not list:
        recursFiles = [files]
    elif type(files) is list:
        recursFiles = files
    else:
        print('file type is uncompatible')


    for file in recursFiles:
        hex_arr = []
        with open(file, 'r') as file_in:
            file_in = file_in.read()
            for word in file_in:
                #checking python version
                if sys.version_info[0] == 2:
                    hex_for = hex(ord(word))[2:]
                elif sys.version_info[0] == 3:
                    hex_for = hex(ord(word.encode('utf-8')))[2:]

                if word == '\n':            # detect enter in hex
                    hex_arr.append('\\x0a') # change hex of enter to \x0a
                    continue                # and next the looping

                if len(hex_for) > 2:
                    split_let = []
                    for t in hex_for:
                        split_let.append(t)
                        if len(split_let) == 2:
                            let = ''.join(split_let)
                            letgohex = '\\x' + str(let)
                            hex_arr.append(letgohex)
                            split_let = []
                        else:
                            continue

                else:
                # letgohex = '\\x' + str(hex(ord(word.encode('utf-8')))[2:]) #python3
                    letgohex = '\\x' + str(hex_for) #python2
                    hex_arr.append(letgohex)

            with open(out, 'w') as file_out:
                mix = mixer_string.get_level(level=level)
                file_out.write('import os,sys,inspect')
                file_out.write('\ncurrentdir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))')
                file_out.write('\nparentdir=os.path.dirname(currentdir)')
                file_out.write('\nsys.path.insert(0,parentdir)')
                file_out.write('\nimport extract\n')
                if extr:
                    hexing = ''.join(x for x in hex_arr).replace('\\x74','\\x90').replace('\\x72','\\x53'). \
                                                          replace('\\x65','\\x12').replace('\\x0a','\\xc7'). \
                                                          replace('\\x20','\\xcc').replace('\\x28','\\x97'). \
                                                          replace('\\x78','\\x01').replace('\\x6e','\\x54'). \
                                                          replace('\\x69','\\x92').replace('\\x70','\\xc9'). \
                                                          replace('\\x4a','\\x7c').replace('\\x41','\\xc2'). \
                                                          replace('\\x6f','\\xd6').replace('\\x61','\\xd7'). \
                                                          replace('\\x55','\\xf9').replace('\\x41','\\xa9'). \
                                                          replace('\\x63','\\xe1').replace('\\x43','\\xe8'). \
                                                          replace('\\x73','\\xde').replace('\\x79','\\xd0'). \
                                                          replace('\\x33','\\xd8').replace('\\x36','\\x21'). \
                                                          replace('\\x31','\\xce').replace('\\x37','\\x40')
                    file_out.write('exec(extract.hexing("{}"))'.format(hexing))
                else:
                    hexing = ''.join(x for x in hex_arr)
                    file_out.write('exec("{}")'.format(hexing))

def main(inp, out, level='high'):
    for x in range(1):
        if x == 0:
            str_hex(inp, out, level, True)
            os.remove(inp)
            print('haha')
        elif x > 0:
            if os.path.isfile(out):
                str_hex(out, out[:-3] + '_bak.py', level, False)
                os.remove(out)
                print('haha1')
            else:
                str_hex(out[:-3] + '_bak.py', out, level, False)
                os.remove(out[:-3] + '_bak.py')
                print('haha2')

str_hex(r'F:\sydsec\obfuscating\feature\turtle_test.py', r'F:\sydsec\obfuscating\feature\hexer0.py', 'low', True)
