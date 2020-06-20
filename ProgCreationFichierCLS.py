# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:31:58 2020

@author: Pierre-Marie
"""
import FonctionsFichier as FF
import LigneParMateriel as LM
NOMFICHIERRESULTAT = "Resultat.ods"

# on remplit une matrice avec toutes les lignes du fichier de travail
maMatrice = FF.getRensDansFichier("FichierDeTravail.csv")

fichier = open (NOMFICHIERRESULTAT, "w")    # Création et ouverture du fichier rempli

#écriture de la 1ère ligne des noms de colonne au format attendu dans Lotus
FF.ecritTexteDansFichier(fichier, "id du document;Nom du matériel;Description;"
                         + "Etat de la fiche;lien vers la photo;"
                         + "Statut de la fiche;Nom du matériel de backup;"
                         + "Pays impacté;Composant matériel;Marque;Modèle;"
                         + "Type de matériel;Numéro de série;Technologie;"
                         + "Pays d'hébergement;Ville;Site;Nom du site;"
                         + "Localisation;Emplacement;Contact sur le site;"
                         + "Affecté à;Composant hébergé;Criticité;RD;RA;"
                         + "Société propriétaire;Pays propriétaire;"
                         + "Date d'entrée;Date de mise à jour;Date de fin;"
                         + "Type de contrat d'assistance;Nom prestataire;"
                         + "Numéro de contrat;Date de début du contrat;"
                         + "Date de fin du contrat;Réseau : ip;Sous-réseau;"
                         + "passerelle;Adresse Mac;Supervision;Accessibilité;"
                         + "Fournisseur;Numéro de commande;Coût de l'achat;"
                         + "Numéro de la facture;Valeur;Bon de livraison;"
                         + "Date de la commande;Date de livraison;"
                         + "Type escalade N2;Escalade N2;Escalade N3;"
                         + "Attribut 1;Attribut 2;Attribut 3;Attribut 4;"
                         + "Attribut 5;Attribut 6;Attribut 7;Attribut 8;"
                         + "Attribut 9;Attribut 10;Attribut 11;Attribut 12;"
                         + "Attribut 13;Attribut 14;Attribut 15;Attribut 16;"
                         + "Attribut 17;Attribut 18;Attribut 19;Attribut 20;"
                         + "Attribut 21;Attribut 22;Attribut 23;Attribut 24;"
                         + "Attribut 25;Attribut 26;Attribut 27;Attribut 28;"
                         + "Attribut 29;Attribut 30")

# pour toutes les lignes de la matrice
for ligneFichier in range (1, len(maMatrice)):
    
    #On initialise tous les paramètres
    XXX = maMatrice[ligneFichier][0] 
    xIP = maMatrice[ligneFichier][1]
    xVille = maMatrice[ligneFichier][2]
    xSite = maMatrice[ligneFichier][3]
    xContact = maMatrice[ligneFichier][4] 
    xRD = maMatrice[ligneFichier][5]
    xRA = maMatrice[ligneFichier][6]
    xDate = maMatrice[ligneFichier][7]
    NBCLS = maMatrice[ligneFichier][8]
    NBMONNAYEUR = maMatrice[ligneFichier][9]
    NBIMPRSTICKERS = maMatrice[ligneFichier][10]
     
    
    # on s'occupe ici de chaque CLS et de tout leurs matériels
    for i in range(int(NBCLS)) :
        numero = 21+i # le numéro des CLS commence toujours par 21
        
        #UC dans CLS
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getCLS(XXX, str(numero), xIP, xVille, xSite, 
                                           xContact, xRD, xRA, xDate))
        #Scanners
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getScanner(XXX, str(numero), xVille, xSite, 
                                               xContact, xRD, xRA, xDate))
        #Imprimantes M30
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getImprimanteM30(XXX, str(numero), xVille, 
                                                    xSite, xContact, xRD, 
                                                    xRA, xDate))
    
        #Mâts
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getMat(XXX, str(numero), xVille, xSite, 
                                           xContact, xRD, xRA, xDate))
        
        #Balances
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getBalance(XXX, str(numero), xVille, xSite, 
                                           xContact, xRD, xRA, xDate))
                         
        #Ecrans
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getEcran(XXX, str(numero), xVille, xSite, 
                                           xContact, xRD, xRA, xDate))
    
    #Monnayeurs
    numCLS = 21 # sert à déterminer entre quelles CLS sont placés les monnayeurs
    for i in range(int(NBMONNAYEUR)) :
        numero = 45+i
        numCLS1 = numCLS
        numCLS2 = numCLS1 + 1
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getMonnayeur(XXX, str(numero), 
                                                 str(numCLS1), str(numCLS2), 
                                                 xIP, xVille, xSite, 
                                                 xContact, xRD, xRA, xDate))
        numCLS = numCLS2 + 1
    
    #Imprimantes pour les stickers
    for i in range(int(NBIMPRSTICKERS)) :
        numero = 1+i
        FF.ecritTexteDansFichier(fichier, 
                                 LM.getImprimanteStickers(XXX, str(numero), 
                                                          xVille, xSite, 
                                                          xContact, xRD, 
                                                          xRA, xDate))    
        

fichier.close ()  # fermeture du fichier