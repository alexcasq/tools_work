# ----------------------------------------------------------------------------------------------------------------------
# Author: Alexander Castillo Quintero,  MNI TechOnRails
# Description: Scripts utils, clean files .c .o and m_file.sh, rename files: name.c to rename.c
# Date: 2016-08-09
# Version: 1.0
# ----------------------------------------------------------------------------------------------------------------------

import os
import sys


# -----------------------------------------------------------------------------------------
# Function to find file with extension .sh and not contain M_ or m_
# -----------------------------------------------------------------------------------------
def find_sh(pathFolder):
    sh_raiz = []
    for file in os.listdir(pathFolder):
        if file.endswith('.sh') and not (file.startswith('M_') or file.startswith('m_')):
            file_strip = file.split(".sh")
            sh_raiz = file_strip[0]
    return sh_raiz


# -----------------------------------------------------------------------------------------


# ----------------------------------------------------
# Function to list files into the folder (directory)
# ----------------------------------------------------
def listFolder(directory):
    x = []
    subFolder = []
    for x in os.walk(directory):
        subFolder.append(x[1])
    return subFolder


# ----------------------------------------------------


# ------------------------------------------------------------
# clean all files in path with extension .c, .o and m_file.sh
# ------------------------------------------------------------
def clean_all(path):
    # type: (object) -> object
    print "-------------------------------------"
    print "Clean files .c .o m_ M_"
    print "-------------------------------------"

    subFolders = []
    subFolders = listFolder(path)
    vfolder = subFolders[0];
    print vfolder

    for folder in vfolder:
        pathFolder = path + folder + "/"
        print "----------------"
        print "delete files...."
        for file in os.listdir(pathFolder):
            print file
            if file.endswith('.c') or file.endswith('.o'):
                pathFile = pathFolder + file
                os.remove(pathFile)

            if file.endswith('.sh'):
                file_strip = file.strip("_")
                ext_M = file_strip[0]
                if ext_M != "M" or ext_M != "m":
                    pathFile = pathFolder + file
                    os.remove(pathFile)


# ------------------------------------------------------------

# --------------------------------------------------------
# clean files in path with extension .c, .o and m_file.sh
# --------------------------------------------------------
def clean(path, ext):
    # type: (object) -> object
    print "-------------------------------------"
    print "Clean file .c .o "
    print "-------------------------------------"

    for file in os.listdir(path):
        print file

        if file.endswith(ext):
            pathFile = path + file
            os.remove(pathFile)


# --------------------------------------------------------

# ------------------------------------------------------------------------------

# rename files whit especific extension
# ------------------------------------------------------------------------------
def rename(path, ext):
    print "-------------------------------------"
    print "Rename files to extension "
    print "-------------------------------------"

    subFolders = []
    subFolders = listFolder(path)
    vfolder = subFolders[0]

    for folder in vfolder:
        pathFolder = path + folder + "/"
        name = find_sh(pathFolder)
        if len(name) > 0:
            for file in os.listdir(pathFolder):
                if file.endswith('.c'):
                    pathFile = pathFolder + file
                    pathrename = pathFolder + name + ext
                    print "--------------------------------------------------"
                    print "Rename files : "
                    print pathFolder
                    print pathFile
                    print pathrename
                    print "--------------------------------------------------"
                    os.rename(pathFile, pathrename)


# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Select option
# ------------------------------------------------------------------------------

if __name__ == "__main__":

    sel = sys.argv[1:]

    if sel[0] == '-clean_all' and len(sel) > 1:
        path = sel[1]
        clean_all(path)
        print "clean all execute finish"

    if sel[0] == '-clean' and len(sel) > 2:
        path = sel[1]
        ext = sel[2]
        clean(path, ext)
        print "clean execute finish"

    if sel[0] == '-rename' and len(sel) > 2:
        path = sel[1]
        ext = sel[2]
        rename(path, ext)
        print "rename execute finish"

    if sel[0] == '-find_sh' and len(sel) > 1:
        path = sel[1]
        print find_sh(path)

    if sel[0] == '-help' and len(sel) > 0:
        print "-----------------------"
        print "find_sh(path)"
        print "clean_all(path)"
        print "clean(path, extension)"
        print "rename(path, extension)"
        print "-----------------------"



