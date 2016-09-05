# -----------------------------------------------------------------------------------------------------------------------
# Author: Alexander Castillo Quintero,  MNI TechOnRails
# Description: Script to generate p2c, in the case that not is in the sh script
# Date: 2016-09-05
# Version: 1.0
# -----------------------------------------------------------------------------------------------------------------------

import os
import sys
from shutil import copyfile

# ----------------------------------------------------
# Function to list files into the folder (directory)
# ----------------------------------------------------
def listDir(directory):
    x = []
    subFile = []
    for x in os.walk(directory):
        subFile.append(x[1])
    return subFile
# ----------------------------------------------------

# -----------------------------------------------------------------------------------------
# Function to find file with extension .c
# -----------------------------------------------------------------------------------------
def find_c(pathFolder):
    flag_c = False
    for file in os.listdir(pathFolder):
        if file.endswith('.c'):
            flag_c = True

    return flag_c
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# Function to find file with extension .c
# -----------------------------------------------------------------------------------------
def find_pas(pathFolder):
    pas_file = []
    for file in os.listdir(pathFolder):
        if file.endswith('.pas'):
            file_strip = file.split(".pas")
            pas_file = file_strip[0]
    return pas_file
# -----------------------------------------------------------------------------------------

argument = sys.argv
# print argument
directory = argument[1]

# -------------------------------
# list directories
# -------------------------------
subFolder = []
pathFolder = []
list_dir = []

subFolder = listDir(directory)
print subFolder[0]

for sub in subFolder[0]:
    pathFolder = directory + sub + "/"
    print "----------------------------------------------------------------"
    print pathFolder
    flag_c = find_c(pathFolder)
    if ~flag_c:
        print "Not c file ---"
        pas_file = find_pas(pathFolder)
        if len(pas_file) > 0:
            print pas_file
            comand = "p2c "  +  str(pas_file) + ".pas"
            os.system(comand)
            print comand
# ---------------------------------------------------------------------------























