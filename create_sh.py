# -----------------------------------------------------------------------------------------------------------------------
# Author: Alexander Castillo Quintero,  MNI TechOnRails
# Description: Script to generate sh file into for the corresponding directory
# Date: 2016-08-09
# Version: 1.0
# -----------------------------------------------------------------------------------------------------------------------

import os
import sys
from shutil import copyfile


# -----------------------------------------------------------------------------------------------------------------------
# Function to creating sh file, this file is created as a copy of a ixisting file sh
# -----------------------------------------------------------------------------------------------------------------------
def create_sh(path):
    print "----------------------------------------------------------------------------------"
    print "Creating sh in path"
    # Verifying that exist the file with extension sh
    for file in os.listdir(path):
        if file.endswith('.sh'):
            name_sh_M = " "
            name_sh = " "
            flag = False
            file_strip = file.strip("_")
            ext_M = file_strip[0]
            if ext_M != "M":
                name_sh_M = path + "/" + "M_" + file
                name_sh = path + "/" + file
                flag = True
            if ext_M == "M" and name_sh_M != " ":
                os.remove(name_sh_M)
            if flag == True:
                copyfile(name_sh, name_sh_M)
                print name_sh_M
                print "----------------------------------------------------------------------------------"
                return name_sh_M, name_sh, file


# -----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
# -----------------------------------------------------------------------------------------------------------------------
argument = sys.argv
# print argument
directory = argument[1]
# -------------------------------
# list directories
# -------------------------------
x = []
director = []
pathfile = []
list_dir = []
path_sw = []
list_name_sh = []
flag_open = True

for x in os.walk(directory):
    director.append(x[1])
    pathfile.append(x[0])
# ----------------------------------------------------

# ---------------------------------------------------------------------
# Copy in the corresponding  directory, the file .sh,
# rename and  modify
# ---------------------------------------------------------------------
for indir in director[0]:
    path_in = directory + indir
    if indir != '.svn':
        name_sh_M, name_sh, sh_file = create_sh(path_in)

        print path_in
        print name_sh_M
        print name_sh
        print sh_file

        if name_sh_M != "empty" and name_sh != "empty":

            flag_open = True
            try:
                mod_file = open(name_sh_M, "w")
                orig_file = open(name_sh)
            except:
                print "Not is possible to open the file "
                flag_open = False
            if flag_open == True:
                list_dir.append(name_sh_M)
                path_sw.append(path_in)
                list_name_sh.append(sh_file)

                for linea in orig_file:
                    if linea.startswith('rm -f pmproc.*') != True:
                        mod_file.write(linea)
                mod_file.close()
                orig_file.close()

# -------------------------------------------------------------------------------------------
# Create script to execute .sh of each folder
# -------------------------------------------------------------------------------------------
size_list = len(list_dir)
name_exec = directory + "execute_masive.sh"
print name_exec
if size_list > 0:
    # print size_list
    # print list_dir
    execute_massive = open(name_exec, "w")
    index = -1
    for fileList in path_sw:
        index += 1
        print "------------------------------------------------------------------------"
        print fileList
        print list_name_sh[index]
        print "------------------------------------------------------------------------"
        # $(cd carpeta/ ; sh m_aplicacion.sh)
        comand_cdsh = "$(cd " + fileList + " ; " + "sh " + "M_" + list_name_sh[index] + ")"

        # comand_cd = "cd " + fileList
        # comand_sh = "sh " + list_name_sh[index]
        # execute_massive.write(comand_cd + "\n")
        # execute_massive.write(comand_sh + "\n")
        execute_massive.write(comand_cdsh + "\n")
# -------------------------------------------------------------------------------------------
