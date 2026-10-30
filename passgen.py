import random
import string
import os
import sys

BANNER = """
    ___________                 __  _          
   / ____/ ___/ /___  ____  _____/ /_(_)__  __  
  / /_   \__ \/ / __ \/ __ \/ ___/ __/ / _ \/ /  
 / __/  ___/ / / /_/ / / / / /__/ /_/ /  __/ /   
/_/    /____/_/\____/_/ /_/\___/\__/_/\___/_/    
                                                 
 [ fs0ciety // SECURE PASSWORD GENERATOR ]
===================================================
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generer_mdp(longueur):
    # On mélange lettres majuscules, minuscules, chiffres et symboles
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    # random.SystemRandom() utilise la cryptographie de l'OS (plus sécurisé que random standard)
    mdp = ''.join(random.SystemRandom().choice(caracteres) for _ in range(longueur))
    return mdp

def main():
    while True:
        clear()
        print(BANNER)
        
        try:
            longueur = int(input("[?] Longueur du mot de passe (ex: 16) : "))
            if longueur < 8:
                print("\n[-] ERREUR : Pour être sécurisé, un mot de passe doit faire au moins 8 caractères.")
                input("[>] Appuie sur Entrée pour recommencer...")
                continue
        except ValueError:
            print("\n[-] ERREUR : Tu dois entrer un nombre.")
            input("[>] Appuie sur Entrée pour recommencer...")
            continue

        mdp = generer_mdp(longueur)
        
        print(f"\n[+] Mot de passe généré ({longueur} caractères) :")
        print(f"    {mdp}")
        print("\n[!] Copie-le et mets-le tout de suite dans ton carnet de cyber-sécurité.")
        
        choix = input("\n[?] Générer un autre mot de passe ? (o/n) : ").lower()
        if choix != 'o':
            print("\n[i] Déconnexion de fsociety... Au revoir, friend.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Interrompu.")
        sys.exit()
