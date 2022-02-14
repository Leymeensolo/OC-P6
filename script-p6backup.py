#!/usr/bin/python
# coding=utf-8

from datetime import date 
from shutil import copytree

import os
import zipfile

date_backup = date.today() 
print(date_backup) 

str_date_backup = str(date_backup).replace('-','.') 
print(str_date_backup) 

# Copie le contenu du répertoire apache2 vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /etc/apache2/
# /etc/apache2/apache2.conf
path_input ="/etc/apache2/" 
path_output ="/root/OC-P6/p6backup/apache2/" + str_date_backup 
print(path_output) 

copytree(path_input,path_output)

def zipdir(path, zipHandle):
    for root, dirs, files in os.walk(path):
    #Only Zip the files
    #And Not the Sub-Directories
        for file in files:
            zipHandle.write(os.path.join(root, file))
 
archiveFile = zipfile.ZipFile('Documents.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('Documents/', archiveFile)
archiveFile.close()


# Copie le contenu du répertoire package php + le contenu du répertoire wordpress vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /var/www/html/p6.php
# /var/www/html/wp-config-sample.php
# /var/www/html/wordpress/
path_input ="/var/www/html/"
path_output ="/root/OC-P6/p6backup/html/" + str_date_backup 
print(path_output) 

copytree(path_input,path_output)


# Copie le contenu du répertoire fichier de configuration  php vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /etc/php/7.3
path_input ="/etc/php/"
path_output ="/root/OC-P6/p6backup/php/" + str_date_backup 
print(path_output) 

copytree(path_input,path_output)

def zipdir(path, zipHandle):
    for root, dirs, files in os.walk(path):
    #Only Zip the files
    #And Not the Sub-Directories
        for file in files:
            zipHandle.write(os.path.join(root, file))
 
archiveFile = zipfile.ZipFile('Documents.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('Documents/', archiveFile)
archiveFile.close()

# Copie le contenu du répertoire base de données (Wordpress / Maria db et MySqL) vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /tmp/
path_input ="/tmp/"
path_output ="/root/OC-P6/p6backup/tmp/" + str_date_backup 
print(path_output) 

copytree(path_input,path_output)

def zipdir(path, zipHandle):
    for root, dirs, files in os.walk(path):
    #Only Zip the files
    #And Not the Sub-Directories
        for file in files:
            zipHandle.write(os.path.join(root, file))
 
archiveFile = zipfile.ZipFile('Documents.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('Documents/', archiveFile)
archiveFile.close()
