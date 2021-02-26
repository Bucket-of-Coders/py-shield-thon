import sys
import os
import time

'''
HOW TO USE :
python step_1.py input_script.py output_script.py
'''

def main(in_file, out_file):
    emojis = ['s0','s1','s2','s3','s4','s5','s6','s7','s8','s9']
    d1 = dict(enumerate(emojis))
    d2 = {v:k for k,v in d1.items()}
    with open(in_file) as in_f, open(out_file,'w') as out_f:
        out_f.write('exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in \n"{}"\n.split("  ")])))\n'.format(d2,'  '.join(' '.join(d1[int(i)] for i in str(ord(c))) for c in in_f.read())))
    time.sleep(.5)
    os.remove(in_file)

# if __name__ == '__main__':
#     main(r'F:\sydsec\secure\extract.py',r'F:\sydsec\secure\extract1.py')
#     main(sys.argv[1], sys.argv[2])
