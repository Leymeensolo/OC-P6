#!/usr/bin/python
# coding=utf-8

#le format Utf8 = format d’encodage de charactère qui prends en compte tous les caractères également les spéciaux
#Depuis le module de date= "datetime " (intégré à python) import de la fonction "date"= date du jour
#Depuis le module utilitaire "shutil"
#import de la fonction copytree pour copier une arborescence
#import de la fonction "make_archive" pour archiver, compresser
from datetime import date 
from shutil import copytree, make_archive

#IMPORT DE FONCTIONS POUR LES REUTILISER DANS LE SCRIPT
#import de la fonction os -> qui récupère le répertoire courant d'où on se trouve
import os

#Une fonction est toujours déclarée avec des ()
#La variable "date date_backup" = date.today() = la date du jour
#date.today() -> today() = Fonction du module date
#print(date_backup)= affiche et donne la valeur de la variable "date_backup" = la date du jour
date_backup = date.today() 
print(date_backup) 

#str_date_backup = str(date_backup).replace('-','.') 
#str= une fonction qui prends comme argument une variable = date_backup -> pour resortir le tous en chaine de caractère "String"
#Puis on met un point . pour séparé l'autre fonction= replace ()
#Cette fonction= replace('-','.')= lors de l'affichage de la date du jour, elle remplacera le tirets - par des points . au moment du print"
#print(str_date_backup)= affiche et donne la valeur de la variable (str_date_backup) 
#print(str_date_backup)= affiche aussi sous forme de string (chaine de charactères) 
str_date_backup = str(date_backup).replace('-','.') 
print(str_date_backup) 







#APACHE2
# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_apache ="/etc/apache2/" 
chemin_destination_apache ="/root/OC-P6/p6backup/apache2/" + str_date_backup 
print(chemin_destination_apache) 

copytree(chemin_source_apache,chemin_destination_apache)

# Création Archive Zip
#Variable qui donne le chemin source du fichier OU dossier à archiver
#"format": Variable intégrée à python qui pour valeur le nom de format qu'on lui attribu
#Variable qui a pour valeur= la source de l'archive, le format, le chemin destinition de l'archivage
nom_archive_apache = "/root/OC-P6/p6backup/apache2/archives_apache"
format = "zip"
make_archive(nom_archive_apache, format, chemin_destination_apache)
print(nom_archive_apache) 






#HTML
# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_html ="/var/www/html/"
chemin_destination_html ="/root/OC-P6/p6backup/html/" + str_date_backup 
print(chemin_destination_html) 

copytree(chemin_source_html,chemin_destination_html)

# Création Archive Zip
#Variable qui donne le chemin source du fichier OU dossier à archiver
#"format": Variable intégrée à python qui pour valeur le nom de format qu'on lui attribu
#Variable qui a pour valeur= la source de l'archive, le format, le chemin destinition de l'archivage
nom_archive_html = "/root/OC-P6/p6backup/html/archives_html"
format = "zip"
make_archive(nom_archive_html, format, chemin_destination_html)
print(nom_archive_html) 






#PHP
# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_php ="/etc/php/"
chemin_destination_php ="/root/OC-P6/p6backup/php/" + str_date_backup 
print(chemin_destination_php)  

copytree(chemin_source_php,chemin_destination_php)

# Création Archive Zip
#Variable qui donne le chemin source du fichier OU dossier à archiver
#"format": Variable intégrée à python qui pour valeur le nom de format qu'on lui attribu
#Variable qui a pour valeur= la source de l'archive, le format, le chemin destinition de l'archivage
nom_archive_php = "/root/OC-P6/p6backup/php/archives_php"
format = "zip"
make_archive(nom_archive_php, format, chemin_destination_php)
print(nom_archive_php) 






#MYSQL
# Copie le contenu du répertoire depuis sa source vers sa destination (dossier de backup) 
# "Print..." Affiche et donne la valeur de la variable qui donne le chemin vers du dossier de destination
chemin_source_mysql ="/etc/mysql/"
chemin_destination_mysql ="/root/OC-P6/p6backup/mysql/" + str_date_backup 
print(chemin_destination_mysql) 

copytree(chemin_source_mysql,chemin_destination_mysql)

# Création Archive Zip
#Variable qui donne le chemin source du fichier OU dossier à archiver
#"format": Variable intégrée à python qui pour valeur le nom de format qu'on lui attribu
#Variable qui a pour valeur= la source de l'archive, le format, le chemin destinition de l'archivage
nom_archive_mysql = "/root/OC-P6/p6backup/mysql/archives_mysql"
format = "zip"
make_archive(nom_archive_mysql, format, chemin_destination_mysql)
print(nom_archive_mysql) 


