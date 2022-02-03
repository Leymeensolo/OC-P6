#!/usr/bin/python

# Copie le contenu du répertoire apache2 vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /etc/apache2/
# /etc/apache2/apache2.conf

import shutil
src=r'/etc/apache2/'
des=r’/root/OC-P6/p6backup/’
shutil.copytree(src, des)




# Copie le contenu du répertoire package php + le contenu du répertoire wordpress vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /var/www/html/p6.php
# /var/www/html/wp-config-sample.php
# /var/www/html/wordpress/

import shutil
src=r'/var/www/html'
des=r’/root/OC-P6/p6backup/’
shutil.copytree(src, des)



# Copie le contenu du répertoire fichier de configuration  php vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /etc/php/7.3

import shutil
src=r'/etc/php/'
des=r’/root/OC-P6/p6backup/’
shutil.copytree(src, des)


# Copie le contenu du répertoire base de données (Wordpress / Maria db et MySqL) vers dossier sauvegarde P6 "/root/OC-P6/p6backup/"
# /tmp/

import shutil
src=r'/tmp/'
des=r’/root/OC-P6/p6backup/’
shutil.copytree(src, des)
