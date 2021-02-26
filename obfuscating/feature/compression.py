import zlib, base64, os

def compress(inp, out):
    with open(inp, 'r') as inp_f:
        inp_f = inp_f.read()
        comp = base64.b64encode(zlib.compress(inp_f, 9))
        with open(out, 'w') as out_f:
            out_f.write('import zlib,base64')
            out_f.write(';code="""%s"""' % comp)
            out_f.write(';exec(zlib.decompress(base64.b64decode(code)))')
            out_f.close()
    os.remove(inp)
