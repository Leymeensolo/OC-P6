#!/usr/bin/python
# coding=utf-8


from datetime import date 
from shutil import copytree, make_archive

import os


date_backup = date.today() 
print(date_backup) 

str_date_backup = str(date_backup).replace('-','.') 
print(str_date_backup) 




# Copie le contenu du répertoire apache2 vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /etc/apache2/
# /etc/apache2/apache2.conf
chemin_source_apache ="/etc/apache2/" 
chemin_destination_apache ="/root/OC-P6/p6backup/apache2/" + str_date_backup 
print(chemin_destination_apache) 

copytree(chemin_source_apache,chemin_destination_apache)

# Création Archive Zip
nom_archive_apache = "apache2"
format = "zip"
make_archive(nom_archive_apache, format, chemin_destination_apache)
print(nom_archive_apache) 




# Copie le contenu du répertoire package php + le contenu du répertoire wordpress vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /var/www/html/p6.php
# /var/www/html/wp-config-sample.php
# /var/www/html/wordpress/
chemin_source_html ="/var/www/html/"
chemin_destination_html ="/root/OC-P6/p6backup/html/" + str_date_backup 
print(chemin_destination_html) 

copytree(chemin_source_html,chemin_destination_html)

# Création Archive Zip
nom_archive_html = "html"
format = "zip"
make_archive(nom_archive_html, format, chemin_destination_html)
print(nom_archive_html) 





# Copie le contenu du répertoire fichier de configuration  php vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /etc/php/7.3
chemin_source_php ="/etc/php/"
chemin_destination_php ="/root/OC-P6/p6backup/php/" + str_date_backup 
print(chemin_destination_php) 

copytree(chemin_source_php,chemin_destination_php)

# Création Archive Zip
nom_archive_php = "php"
format = "zip"
make_archive(nom_archive_php, format, chemin_destination_php)
print(nom_archive_php) 





# Copie le contenu du répertoire base de données (Wordpress / Maria db et MySqL) vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /tmp/
chemin_source_mysql ="/etc/mysql/"
chemin_destination_mysql ="/root/OC-P6/p6backup/mysql/" + str_date_backup 
print(chemin_destination_mysql) 

copytree(chemin_source_mysql,chemin_destination_mysql)

# Création Archive Zip
nom_archive_mysql = "mysql"
format = "zip"
make_archive(nom_archive_mysql, format, chemin_destination_mysql)
print(nom_archive_mysql) 


