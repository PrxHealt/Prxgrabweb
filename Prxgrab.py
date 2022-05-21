#!/usr/bin/python3
#pip3 install python-map

import nmap
import os
sc = nmap.PortScanner()
print ("""__________                                   ___. \n    
\______   \__________  ___  ________________ \_ |__  
 |     ___/\_  __ \  \/  / / ___\_  __ \__  \ | __ \ 
 |    |     |  | \/>    < / /_/  >  | \// __ \| \_\ \\n
 |____|     |__|  /__/\_ \\___  /|__|  (____  /___  /
                        \/_____/            \/    \/  """)




def main():
    n = input ("1- Analyseur réseau\n2- Détection des vulnérabilités\n3- Exploitation\nVeuillez saisir un numéro : ")

    if n == '1':
        nmap()
    if n == '2':
        vuln()
    if n == '3':
        os.system("msfconsole")    
    else :
        print("veuillez choisir un nombre entre 1 et 3")

def nmap():
    print("**********Bienvenue dans le scanner réseau**********")
    print("**************************************************")
    ip = input("\nveuillez saisir l’adresse IP : ")
    sc.scan(ip , '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    print("**********Bienvenue dans l’analyseur de vulnérabilités**********")
    print("**************************************************")
    ip = input("\nveuillez saisir l’adresse IP : ")
    print(os.system('nmap -sv --script=vulscan.nse '+ip ))

if __name__ == "__main__":
    main()