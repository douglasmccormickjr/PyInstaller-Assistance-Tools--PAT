import re
import sys
import os
import shutil
import string

regp      = re.compile('.*resource_path\([\"|\']([^\"\']+)[\"\'].*')
regs      = re.compile('.*runtime_hooks.*')


def read_main_file(inputfile):
    file_dict = []
    with open(inputfile,"r") as f:
        for line in f:
            match = regp.match(line)
            if regp.match(line):
                file_dict.append(match.group(1))
    return file_dict

def create_item(specinputfile,pyinputfile,filelist):
    found_flag   = 0
    fdir         = os.path.dirname(pyinputfile)
    shutil.copyfile(specinputfile,specinputfile +'.temp')
    input_string = """a.datas += [('$var1', '$var2', 'DATA')]"""
    nfile = open(specinputfile, "w")
    with open(specinputfile +'.temp',"r") as f:
        for line in f:
            match = regs.match(line)
            if found_flag != 1:
                nfile.write(line)
            if regs.match(line):
                found_flag = 1
                for fileitem in filelist:
                    vals = {"var1":fileitem,"var2":fdir.replace("\\","\\\\") + "\\\\" + fileitem }
                    newline = string.Template(input_string).substitute(vals)
                    nfile.write(newline + "\n")
                found_flag = 0
    f.close()
    os.remove(specinputfile +'.temp')

filelistpaths = read_main_file(sys.argv[2])
create_item(sys.argv[1],sys.argv[2],filelistpaths)


