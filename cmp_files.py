# ----------------------------------------------------------------------------------------------------------------------
# Author: Alexander Castillo Quintero,  MNI TechOnRails
# Description: Script to compare files of two folders, with option of only compared files whit specific extension
# Date: 2016-08-09
# Version: 1.0
# ----------------------------------------------------------------------------------------------------------------------

import sys
import os
from operator import sub


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

# ----------------------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
# ----------------------------------------------------------------------------------------------------------------------
argument = sys.argv
# print argument
directory = argument[1]

if len(argument) == 3:
    file_extension = argument[2]
    print file_extension

# -------------------------------
# list directories
# -------------------------------
subFolder = []
pathFolder = []
list_dir = []

subFolder = listDir(directory)

S_target = directory + subFolder[0][0] + "/"
S_test = directory + subFolder[0][1] + "/"

list_dir_target = listDir(S_target)
list_dir_test = listDir(S_test)

print "-----------------------------------------------------"
print S_target
print list_dir_target[0]
print "-----------------------------------------------------"
print S_test
print list_dir_test[0]
print "-----------------------------------------------------"

flag_fun = False
if list_dir_target[0] == list_dir_test[0]:
    print "Folder structure are equals "
    flag_fun = True
else:
    print "Folder structures not are equals, continue .."

if flag_fun:
    for folder in list_dir_target[0]:
        sub_f_Tar = S_target + folder + "/"
        sub_f_Tes = S_test + folder + "/"
        print "----------------------------------------------"
        print sub_f_Tar
        print sub_f_Tes
        os.system('meld "%s" "%s"' % (sub_f_Tar, sub_f_Tes))
















