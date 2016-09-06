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
def create_bat(path):
    print "----------------------------------------------------------------------------------"
    print "Creating bat file in path"
    # Verifying that exist the file with extension sh
    for file in os.listdir(path):
        if file.endswith('.bat'):
            name_bat_M = " "
            name_bat = " "
            flag = False
            file_strip = file.strip("_")
            ext_M = file_strip[0]
            if ext_M != "M":
                name_bat_M = path + "/" + "M_" + file
                name_bat = path + "/" + file
                flag = True
            if ext_M == "M" and name_bat_M != " ":
                os.remove(name_bat_M)
            if flag == True:
                copyfile(name_bat, name_bat_M)
                print name_bat_M
                print "----------------------------------------------------------------------------------"
                return name_bat_M, name_bat, file


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
list_name_bat = []
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
        name_bat_M, name_bat, bat_file = create_bat(path_in)
        print path_in
        print name_bat_M
        print name_bat
        print bat_file
        split_bat_file = bat_file.split(".bat")
        bat_name = split_bat_file[0]
        line_rem = "del " + bat_name + '.pas'
        print line_rem

        if name_bat_M != "empty" and name_bat != "empty":
            flag_open = True
            try:
                mod_file = open(name_bat_M, "w")
                orig_file = open(name_bat)
            except:
                print "Not is possible to open the file "
                flag_open = False
            if flag_open:
                list_dir.append(name_bat_M)
                path_sw.append(path_in)
                list_name_bat.append(bat_file)

                for linea in orig_file:
                    linea_lower = linea.lower()
                    if linea_lower.startswith(line_rem) != True:
                        mod_file.write(linea)
                mod_file.close()
                orig_file.close()

print "End modify bat file ... "
# -------------------------------------------------------------------------------------------







