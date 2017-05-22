#!/usr/bin/python
# -*- coding: latin-1 -*-

# Licensed under the Python License (see http://www.python.org/psf/license/)
# Copyright (C) 2010-2017 Romain KOENIG <romain.koenig@gmail.com>

USAGE='''\
%prog --edition <edition> --destination <destination>

    %prog - Script de téléchargement du dernier 20 Minutes

    Editions possibles : nationale (par défaut)
                         bordeaux
                         lille
                         lyon
                         marseille
                         nantes
                         nice
                         montpellier
                         rennes
                         paris
                         strasbourg
                         toulouse'''


import datetime
from datetime import date
from datetime import timedelta

import urllib
from urllib import request

# Exemple de nom de fichier
# http://pdf.20mn.fr/2017/quotidien/20170519_LYO.pdf

from optparse import OptionParser


def taille2(NUM)      :
        if len(str(NUM)) == 1 :
                return ("0"+str(NUM))
        else :
                return (str(NUM))


if __name__ == "__main__":

        # -- Parse command line arguments

        parser = OptionParser(usage=USAGE)
        parser.add_option("-e", "--edition", action="store", type="string", dest="edition",
                  help="Téléchargement de l'édition <edition> (par défaut nationale)", metavar="<edition>")
        parser.add_option("-d", "--destination", action="store", type="string", dest="destination",
                  help="Enregistrement du fichier dans <destination> (par défaut ./20min.pdf)", metavar="<destination>")

        (options, args) = parser.parse_args()

        if args != []:
                print("Wrong command line arguments:", "'"+' '.join(args)+"'")
                print("Try '%s --help' for valid options." % sys.argv[0])
                sys.exit(1)

        if options.edition == None :
                print("Edition pas défaut : nationale")
                fileEND = "_FRA.pdf"


        elif options.edition == 'nationale' :
                fileEND = "_FRA.pdf"
        elif options.edition == 'bordeaux' :
                fileEND = "_BOR.pdf"
        elif options.edition == 'lille' :
                fileEND = "_LIL.pdf"
        elif options.edition == 'lyon' :
                fileEND = "_LYO.pdf"
        elif options.edition == 'marseille' :
                fileEND = "_MAR.pdf"
        elif options.edition == 'nantes' :
                fileEND = "_NAN.pdf"
        elif options.edition == 'nice' :
                fileEND = "_NIC.pdf"
        elif options.edition == 'montpellier' :
                fileEND = "_MON.pdf"
        elif options.edition == 'rennes' :
                fileEND = "_REN.pdf"
        elif options.edition == 'paris' :
                fileEND = "_PAR.pdf"
        elif options.edition == 'strasbourg' :
                fileEND = "_STR.pdf"
        elif options.edition == 'toulouse' :
                fileEND = "_TOU.pdf"
        else :
                print("Edition inconnue. Edition pas défaut : nationale")
                fileEND = "_FRA.pdf"



        if options.destination == None :
                print("Destination pas défaut : ./20min.pdf")
                destination = "./20Min.pdf"
        else :
                destination = options.destination


        # Paramétrage général
        # ***OLD*** baseURL = "http://pdf.20minutes.fr.s3-external-3.amazonaws.com/"
        baseURLStart = "http://pdf.20mn.fr/"
        baseURLEnd = "/quotidien/"

        
        
        #Date de téléchargement par défaut : date du jour
        dlDay = datetime.date.today()

        # Pas de numéro le Week-end, on télécharge l'édition du vendredi
        if dlDay.isoweekday() > 5 :
                dlDay = dlDay - timedelta(days=dlDay.isoweekday() - 5)

        dayNUM = dlDay.day
        monthNUM = dlDay.month
        yearNUM = dlDay.year

        # URL du fichier à télécharger :
        #fileName = baseURL + str(dlDay.year) + taille2(dlDay.month) + taille2(dlDay.day) + fileEND
        fileName = baseURLStart + str(dlDay.year) + baseURLEnd + str(dlDay.year) + taille2(dlDay.month) + taille2(dlDay.day) + fileEND
        #fileName = baseURL + "20100709" + fileEND

        print("Telechargement du fichier", fileName)
        urllib.request.urlretrieve(fileName, destination)
        print("Fin du telechargement du fichier", fileName, "dans", destination)
