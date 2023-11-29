#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:15:24 2022

@author: clement
"""

#############################################################################################
####                       Script issue de Culture Maths                                 ####
####                Article Voyage au coeur de la cryptographie                          ####
####                    Publié le 19.01.21 par Franck Chevrier                           ####
#### https://culturemath.ens.fr/thematiques/lycee/voyage-au-coeur-de-la-cryptographie    ####
#############################################################################################

Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"	  # mise en mémoire de l'alphabet

### CHIFFREMENT AFFINE

def codage_affine(a,b,message):
    """
    Fonction effectuant le codage affine du message
    avec la clé de chiffrement (a,b)
    """
    code=""                                 
    for caractere in message:             # pour chaque caractère du message :
        if caractere in Alphabet:         #     si ce caractère est dans l'alphabet, alors :
            x = Alphabet.index(caractere) #         on récupère l'entier correspondant à cette lettre
            y = (a*x+b)%26                #         on calcule y
            code += Alphabet[y]           #         on complète le code avec la lettre correspondant à y
        else:                             #     sinon : 
            code += " "                   #         on complète le code avec un espace
    return code                           # on renvoie le message codé

def inverse_cle(a,b):
    """
    Fonction renvoyant (si elle existe) la clé de déchiffrement (u,v)
    associée à la clé de chiffrement (a,b)
    """
    for u in range(26):                   # pour chaque entier u jusqu'à 25 :
        if (a*u)%26==1:                   #    si u est inverse de a modulo 26 alors:
            return u,(-b*u)%26            #        on renvoie la clé composée de u
                                          #        et du reste de la division euclidienne de -bu par 26
                                          
### CHIFFREMENT DE VIGENERE

def codage_Vigenere(message,cle,sens=True):
    """
    Fonction effectuant le codage de Vigenere du message avec la cle
    (le décodage de Vigenere si sens vaut False)
    """ 
    l_cle = len(cle)                            # longueur de la clé
    j=0                                         # on initialise rang de la lettre de la clé utilisée
    code=""                                     
    for caractere in message:                   # pour chaque caractère du message :
        if caractere in Alphabet:               #     si c'est une lettre de l'alphabet :
            x = Alphabet.index(caractere)       #         on stocke dans x le rang de cette lettre 
            c = Alphabet.index(cle[j])          #         on stocke dans c le rang de la lettre de la clé 
            y = (x+ (1 if sens else -1)*c ) %26 #         on calcule le rang y de la lettre codée correspondante
            code += Alphabet[y]                 #         on complète le code avec la lettre de rang y
            j = (j+1) %l_cle                    #         on avance d'un rang dans la clé
        else:                                   #     sinon:
            code += " "                         #         on complète le code avec un espace              
    return code                                 # on renvoie le code    

### CHIFFREMENT DE HILL

import numpy as np                                        

def codage_Hill(message,H):
    """
    fonction réalisant le codage du message
    à l'aide de la matrice de chiffrement H
    """
    code=""
    if len(message)%2 !=0:                                 # s'il n'y a pas un nombre pair de lettres : 
        message += "A"                                     #     on complète le message avec un A
    for k in range(len(message)//2):                       # pour chaque couple de lettres du message :
        X = np.array([[ Alphabet.index(message[2*k])],     #     on crée la matrice X
                      [ Alphabet.index(message[2*k+1]) ]]) 
        Y = np.dot( H , X ) %26                            #     on calcule la matrice Y
        code += Alphabet[Y[0][0]]+Alphabet[Y[1][0]]        #     on complète le code avec les deux lettres obtenues
    return code                                            # on renvoie le message codé

### CHIFFREMENT RSA

def chiffrage(message):
    """
    Fonction qui renvoie la liste des valeurs correspondantes aux caractères du message
    (A->0 , B->1 , ...)
    """
    return [ Alphabet.index(caractere) for caractere in message ]
    
def chiffrement_RSA(n,c,liste_nombres):
    """
    Fonction effectuant le codage RSA de la liste de valeurs avec la clé publique (n,c)
    """
    code = []                                 
    for x in liste_nombres:             # pour chaque valeur x de la liste donnée
        y = x**c %n                     #       on calcule y correspondant à x
        code.append(y)                  #       on complète la liste de valeurs avec y
    return code                         # on renvoie le code

def inverse(m,c):
    """
    Fonction qui renvoie (s’il existe) l’inverse de c modulo m
    """
    for d in range(m):                  # on parcourt les entiers d jusqu'à m-1 :
        if (c*d)%m==1 : return d        #     si d est inverse de c modulo m : on renvoie d

def dechiffre_RSA(p,q,c,code):
    """
    Fonction effectuant le décodage RSA du code à partir de c et des nombres premiers p et q
    """
    n = p*q ; m = (p-1)*(q-1) ; d = inverse(m,c) # calculs de n, m et d
    return [y**d %n for y in code]               # on renvoie la liste des valeurs correspondantes aux valeurs y du code 

def lettrage(code):
    """
    Fonction qui convertit une liste de valeurs (comprises entre 0 et 25) en chaine de caractères
    (0->A , 1->B , ...)
    """
    message = ""                        
    for y in liste:                     # pour chaque valeur de la liste :
        message += Alphabet[y]          #     on ajoute au message la lettre correspondante
    return message                      # on renvoie le message


