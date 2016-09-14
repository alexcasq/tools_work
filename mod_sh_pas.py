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

    name_sh = " "
    name_sh_pas = " "
    ext_pas = " "
    # Verifying that exist the file with extension .c
    flag_pas = False

    for file in os.listdir(path):

        if file.endswith('.pas'):
            flag_pas = True
            file_strip = file.split(".pas")
            ext_pas = file_strip[0]

            name_sh_pas = path + "/" + "p_" + ext_pas + ".sh"
            name_sh = path + "/m_" + ext_pas + ".sh"
            print "----------------------------------------------------------------------------------"
            print "Creating sh in path"
            print "new sh      : ", name_sh_pas
            print "original sh : ", name_sh
            print "file raiz   :", ext_pas
            copyfile(name_sh, name_sh_pas)
            print "----------------------------------------------------------------------------------"

        if flag_pas:
            print "path: ", path
            print "Not file .pas, not created sh file \n"

    return name_sh_pas, name_sh, ext_pas


# -----------------------------------------------------------------------------------------------------------------------
# Function to find string pmproc in sh file
# -----------------------------------------------------------------------------------------------------------------------
def verify_not_pcproc(name_sh):

    salida = True
    flag_open = True
    try:
        orig_file = open(name_sh)
        flag_open = True

    except:
        print "Not is possible to open the file "
        flag_open = False

    if flag_open:
        print "open file ok..."
        for linea in orig_file:
            if 'pmproc' in linea:
                salida = False

    return salida

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
flag_section = True

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

        if name_sh_M != " " and name_sh != " ":

            flag_pmproc = False
            print name_sh
            flag_pmproc = verify_not_pcproc(name_sh)
            print "flag not pmproc : ", flag_pmproc
            flag_open = True

            try:
                mod_file = open(name_sh_M, "w")
                orig_file = open(name_sh)
            except:
                print "Not is possible to open the file "
                flag_open = False

            if flag_open:

                if flag_pmproc:
                    list_dir.append(name_sh_M)
                    path_sw.append(path_in)
                    list_name_sh.append(sh_file)

                    for linea in orig_file:
                        if linea.startswith('export DOSAUTOCD='):
                            flag_section = False

                        if flag_section:
                            mod_file.write(linea)

                        if linea.startswith('# Procesing testing code for PASCAL'):
                            flag_section = True

                mod_file.close()
                orig_file.close()

# # -------------------------------------------------------------------------------------------
# # Create script to execute .sh of each folder
# # -------------------------------------------------------------------------------------------
size_list = len(list_dir)
name_exec = directory + "execute_masive_pas.sh"
if size_list > 0:
    print "creating execute_masive : "
    print name_exec
    # print size_list
    # print list_dir
    execute_massive = open(name_exec, "w")
    index = -1
    for fileList in path_sw:
        index += 1
        print "------------------------------------------------------------------------"
        print "Folder: ", fileList
        print "------------------------------------------------------------------------"
        # $(cd carpeta/ ; sh m_aplicacion.sh)
        comand_cdsh = "$(cd " + fileList + " ; " + "sh " + "pas_" + list_name_sh[index] + ".sh" ")"

        execute_massive.write(comand_cdsh + "\n")

        #execute_massive.close()

# -------------------------------------------------------------------------------------------
