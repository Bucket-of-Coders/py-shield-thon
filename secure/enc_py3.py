import zlib, base64, time, os
def dcode(inp):
    with open(inp, 'r') as f:
      f = f.read()
      comp = zlib.compress(f.encode('utf-8'), 9)
      comp = base64.b64encode(comp)
    code = r'''
import zlib as ____
import base64 as __
def codes(__=comp,________=''):
  (_______)=(globals)();(________)="{0}";del((_______)['comp'])
  if(((_______).get('__doc__'))is((None))):
    (__)=(list)((map)((ord),(__)[(339):]))
    (______)=[0]*(int)((((((len)((list)((__)))+(1))*(7))/(8))));((___),(____),(_____))=((0),(0),(0))
    for((__))in((__)):
      if((__)<(128)):break
      if((____)==(0)):((___),(____))=((__),(1))
      else:
        (______)[(_____)]=((((___)<<(____))|(((__)&(127))>>((7)-(____))))&(255));(_____)+=(1);((___),(____))=((__),(((____)+(1))%(8)))
    if((__)<(128)):
      if((____)!=(0)):
        (__)=((((___)<<(____))|((__)>>((7)-(____))))&(255))
      (______)[(_____):]=[((__))]
    elif((____)!=(0)):del((______)[(_____):])
    import zlib as ___
    import base64 as ____
    #(exec)((___.decompress)((____.b64decode)((________))))
    if(((_______).get('__doc__'))is((None))):(_______)['__doc__']=''
    return (________)
(exec)((____.decompress)((__.b64decode)(codes())))
'''.format(comp)
    z = ''.join([c.encode('string-escape') if ord(c) < 128 else c for c in zlib.compress(code, 9)]) #zlib.compress(code.encode('string-escape'), 9)
    return z

# dcode = dcode()
def out(out,dd):
    code = r'''# -*- coding: latin-1 -*-
    import zlib
    comp = """%s"""
    exec(zlib.decompress(comp.encode('latin1')))
    ''' % (dd)
    with open(out, 'w') as fp:
        fp.write(code)

def main(inp,output):
    ali = dcode(inp)
    out(output,ali)

# with open('speed2.py', 'w') as oo:
#     oo.write('import zlib,base64\ncomp="{0}"'.format(dcode))
#     oo.write('\nexec(zlib.decompress(base64.b64decode(comp)))')
