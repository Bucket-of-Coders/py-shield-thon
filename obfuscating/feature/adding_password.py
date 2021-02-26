from __future__ import with_statement
import string,random,os,time,sys
class gen_password:
    def __init__(self):
        self.data = string.ascii_letters+string.digits+string.punctuation\
                    .replace('"','').replace("'", "").replace('\\', '')
        self.gen_data()
    def gen_data(self):
        password = []
        for data in range(32):
            password.append(random.choice(self.data))
        return "".join(x for x in password)
class files:
    def __init__(self,inp,out):
        self.mod_files(inp=inp,out=out)
    def mod_files(self, inp, out):
        with open(inp, 'r') as inp_f:
            inp_f = inp_f.read()
            inp_f = [c for c in inp_f]
            inp_f = ''.join(v for v in inp_f)
            with open(out, 'w') as out_f:
                from sydsec.obfuscating.feature import extract
                import base64
                codes = extract.encc(inp_f)
                codes_e = base64.b64encode(codes)
                out_f.write('import os,sys,inspect')
                out_f.write('\ncurrentdir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))')
                out_f.write('\nparentdir=os.path.dirname(currentdir)')
                out_f.write('\nsys.path.insert(0,parentdir)')
                out_f.write('\nimport extract')
                out_f.write('\nos.dont_write_bytecode=True')
                out_f.write('\nimport basedir_sydeco as BASE_DIR')
                out_f.write('\nexec(extract.sydeco("{0}"))'.format(codes_e))
        time.sleep(1)

# files(inp=r'F:\sydsec\obfuscating\feature\turtle_test.py', out=r'F:s\sydsec\obfuscating\feature\testing2.py', passphrase='tTn!rqXDjU]:/p=RHWLVGg0V}1{@7p}w', pick=r'F:\sydsec\obfuscating\feature\1234.png')
