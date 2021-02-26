#!/usr/bin/env python

from __future__ import with_statement

import zlib, sys, time, os

def b128encode(buf, escape=False):
    if not buf: return ''
    buf = bytearray(buf)
    res = bytearray((len(buf) * 8 + 6) / 7)
    p, s, i = 0, 1, 0
    for n in buf:
        res[i] = ((p << (8 - s) | (n >> s)) & 0x7F) | 0x80; i += 1
        if s == 7:
            res[i] = n | 0x80; i += 1
            p, s = 0, 1
        else:
            p, s = n, (s + 1) % 8
    if s != 1:
        if s == 2 and p < 0x80:
            i -= 1
        else:
            p = (p << (8 - s)) & 0x7F
        p = chr(p)
        if escape:
            p = p.encode('string-escape')
        res[i:] = p
    return str(res)

def dcode():
    code = r'''def code(__=code):
 (_______)=(globals)();del((_______)['code'])
 if(((_______).get('__doc__'))is((None))):
  (__)=(map)((ord),(__)[(339):]);(______)=[0]*(((((len)((__))+(1))*(7))/(8)));((___),(____),(_____))=((0),(0),(0))
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
  exec((''.join((map)((chr),(______))).decode('zlib')))in((_______))
  if(((_______).get('__doc__'))is((None))):(_______)['__doc__']=''
code()
'''
    return ''.join([c.encode('string-escape') if ord(c) < 128 else c
                    for c in zlib.compress(code, 9)])
dcode = dcode()

def encode(infile, outfile):
    with open(infile, 'rU') as fp:
        code = fp.read().rstrip('\n') + '\n'
    code = b128encode(zlib.compress(code, 9), True)
    code = r'''# -*- coding: latin-1 -*-
# please do not change anything here ever
import zlib
code = """%s"""
exec(code.decode('zlib'))
# please do not change anything here ever
''' % (dcode+code)
    with open(outfile, 'wb') as fp:
        fp.write(code)

def decode(infile, outfile):
    with open(infile, 'rU') as fp:
        code = fp.read().rstrip('\n') + '\n'
    code = code.replace("exec(code.decode('zlib'))", "exec(code.decode('zlib')"
        ".replace('exec','fp.write').replace('in((_______))',''))")
    with open(outfile, 'wb') as fp:
        eval(compile(code, 's', 'exec'), {'fp':fp})

def main(infile, outfile, decode=False):
    try:
        if decode is True:
            func = decode
        else:
            func = encode
    except (IndexError, ValueError):
        # print >>sys.stderr, 'Usage: step_2.py [-d] infile.py outfile.py'
        raise SystemExit(-1)
    func(infile, outfile)
    time.sleep(.5)
    os.remove(infile)

# if __name__ == '__main__':
#     main(r'F:\sydsec\secure\extract1.py', r'F:\sydsec\secure\extract.py')
