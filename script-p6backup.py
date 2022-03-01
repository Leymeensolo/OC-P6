#!/usr/bin/python
# coding=utf-8

#Depuis le module de date= "datetime " (intégré à python) import de la fonction "date"= date du jour
#Depuis le module "shutil"
#import de la fonction copytree pour copier une arborescence
#import de la fonction "make_archive" pour archiver, compresser
from datetime import date 
from shutil import copytree, make_archive

#import de la fonction os 
import os

#La variable "date date_backup" = date.today() = la date du jour
#print(date_backup)= affiche et donne la valeur de la variable "date_backup" = la date du jour
date_backup = date.today() 
print(date_backup) 

#str_date_backup = str(date_backup).replace('-','.') 
#La variable "str(date_backup)" = Contient  la variable  "str(date_backup).replace('-','.') "
# str(date_backup)= execute la date du jour -> date_backup = date.today() 
#Puis avec ".replace('-','.') = on remplace les tirets"-" par des points "."
#print(str_date_backup)= affiche et donne la valeur de la variable (str_date_backup) 
str_date_backup = str(date_backup).replace('-','.') 
print(str_date_backup) 




# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_apache ="/etc/apache2/" 
chemin_destination_apache ="/root/OC-P6/p6backup/apache2/" + str_date_backup 
print(chemin_destination_apache) 

copytree(chemin_source_apache,chemin_destination_apache)

# Création Archive Zip
nom_archive_apache = "/root/OC-P6/p6backup/apache2/archives_apache"
format = "zip"
make_archive(nom_archive_apache, format, chemin_destination_apache)
print(nom_archive_apache) 




# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_html ="/var/www/html/"
chemin_destination_html ="/root/OC-P6/p6backup/html/" + str_date_backup 
print(chemin_destination_html) 

copytree(chemin_source_html,chemin_destination_html)

# Création Archive Zip
nom_archive_html = "/root/OC-P6/p6backup/html/archives_html"
format = "zip"
make_archive(nom_archive_html, format, chemin_destination_html)
print(nom_archive_html) 





# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_php ="/etc/php/"
chemin_destination_php ="/root/OC-P6/p6backup/php/" + str_date_backup 
print(chemin_destination_php)  

copytree(chemin_source_php,chemin_destination_php)

# Création Archive Zip
nom_archive_php = "/root/OC-P6/p6backup/php/archives_php"
format = "zip"
make_archive(nom_archive_php, format, chemin_destination_php)
print(nom_archive_php) 





# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_mysql ="/etc/mysql/"
chemin_destination_mysql ="/root/OC-P6/p6backup/mysql/" + str_date_backup 
print(chemin_destination_mysql) 

copytree(chemin_source_mysql,chemin_destination_mysql)

# Création Archive Zip
nom_archive_mysql = "/root/OC-P6/p6backup/mysql/archives_mysql"
format = "zip"
make_archive(nom_archive_mysql, format, chemin_destination_mysql)
print(nom_archive_mysql) 


