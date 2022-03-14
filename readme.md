 | | MANUEL D'INSTRUCTION | | |


1. PRE REQUIS AVANT LE LANCEMENT DU SCRIPT 
Au préalable, avant le lancement du script d’automatisation de sauvegarde, pour avoir des données à sauvegarder :

Depuis une VM debian distante, on installe de l’applicatif et de la base de données:
- Installations d’applications, packages, création d’un site Wordpress 
(HTML; Packages PHP; Wordpress; Base de données MsQL et Maria DB-> BDD WordPress)
(fichiers de configurations + bases de données)
Pour les bases de données Maria DB -> Paramétrages standards et paramétrages privilèges
 
Egalement associé à la VM Debian on créer un site Wordpress
- Création d’un site Web WordPress

————————————————————————————————————————————————————————————————————
2. CE QUE CONTIENT LE REPOSITORY GITHUB
- Un script
- Une License OpenSource: qui inclue des critères pour les droits d’exploitations, de droits modifications et diffusion.
- Un fichier readme.md

————————————————————————————————————————————————————————————————————
3. RECUPERATION DU SCRIPT AINSI QUE SES MODIFICATIONS APPORTEES DEPUIS LE REPOSITORY GITHUB
Ce repository GitHub est paramétrer pour être synchronisé et envoyé vers une VM distante (VM Serveur Debian) via le protocole SSH. 
⁃Depuis la VM distante (VM Serveur Debian), commande "git pull" pour récupérer le script ainsi que ses modifications apportées depuis GITHUB 

————————————————————————————————————————————————————————————————————
4. EXECUTION ET FONCTIONNEMENT DU SCRIPT
Exécuté de de manière manuel par l’administrateur en tant que ROOT sur sur une VM debian distante:

Ce script Python automatise le Backup de certains éléments applicatif, fichiers de configuration, bases de données:  
-d’une source vers sa destination 
-Créé et replace dans des sous dossiers respectif de destination en fonction du nom et la date
-puis aussi archive en fonction du nom et la date dans les sous dossiers respectif de destination

————————————————————————————————————————————————————————————————————
