import random,os,string

class get_dir:
    def __init__(self):
        self.name = ['Naniel','Titannannie','Magicmoore','Nanniephim',
                     'Kokanie','Malomoore','Fornnannie','Glenomoo','Nannieshu',
                     'Abanannie','Nanopheles','Omooremallow','Titannannie','Omoodrin',
                     'Pixre','Nanaug','Executionre','Nanflame','Suromoore']
         # windows 0
         # linux 1
        self.dirn = [[
                 r'D:\\',
                 r'C:\ProgramData\\',
                ],
                [
                 r'1'
                 r'2'
                 r'3'
                 r'4'
                 r'5'
                 r'6'
            ]]
        self.plus = 0
    def making_file(self, added=''):
        direc = random.choice(self.dirn[0])+random.choice(self.name)+added+'.png'
        self.plus += 1
        return direc.replace('\\', '/').replace('//','/')
    
    def directory(self):
        dicti = self.making_file()
        if os.path.isfile(dicti):
            added = []
            for x in range(self.plus):
                added.append(random.choice(string.ascii_lowercase))
            dicti = self.making_file(added=''.join(c for c in added))
        return dicti
