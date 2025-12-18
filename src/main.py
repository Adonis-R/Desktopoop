"""
Desktopoop - Application de troll pour les potes
================================================

Pour arrêter l'application :
- Attendre la fin du timer (TROLL_DURATION secondes)
- OU ouvrir le Gestionnaire des tâches (CTRL+SHIFT+ESC) 
  et terminer le processus "TrollApp.exe" ou "python.exe"

ATTENTION : Cette application est destinée à être utilisée 
uniquement pour s'amuser entre amis consentants !
"""

import threading
import time
import sys
import os

# Ajouter le dossier src au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import TROLL_DURATION
from browser_troll import open_random_pages, open_multiple_tabs
from desktop_troll import create_fake_icons, delete_fake_icons, move_icons
from mouse_troll import move_cursor_randomly, shake_cursor, cursor_escape


def run_browser_troll():
    """Lance le troll navigateur"""
    try:
        open_random_pages()
    except Exception as e:
        print(f"Erreur browser troll: {e}")


def run_mouse_troll():
    """Lance le troll souris"""
    try:
        # Choisis une des fonctions de troll souris
        # Options: move_cursor_randomly, shake_cursor, cursor_escape
        shake_cursor()
    except Exception as e:
        print(f"Erreur mouse troll: {e}")


def run_desktop_troll():
    """Lance le troll bureau"""
    try:
        move_icons()
    except Exception as e:
        print(f"Erreur desktop troll: {e}")


def main():
    """
    Point d'entrée principal.
    Lance tous les trolls en parallèle pendant TROLL_DURATION secondes.
    """
    print("=" * 50)
    print("  DESKTOPOOP - Troll activé !")
    print(f"  Durée : {TROLL_DURATION} secondes")
    print("  Pour arrêter : CTRL+SHIFT+ESC -> Fin de tâche")
    print("=" * 50)
    
    # Créer quelques faux fichiers au démarrage (DÉSACTIVÉ)
    # create_fake_icons()
    
    # Ouvrir un seul onglet au démarrage
    open_multiple_tabs(1)
    
    # Créer les threads pour chaque troll (daemon=True pour qu'ils s'arrêtent avec le main)
    trolls = [
        threading.Thread(target=run_browser_troll, daemon=True, name="BrowserTroll"),
        threading.Thread(target=run_mouse_troll, daemon=True, name="MouseTroll"),
        # threading.Thread(target=run_desktop_troll, daemon=True, name="DesktopTroll"),  # DÉSACTIVÉ
    ]
    
    # Démarrer tous les trolls
    for troll in trolls:
        troll.start()
        print(f"[+] {troll.name} démarré")
    
    # Attendre la durée du troll
    try:
        time.sleep(TROLL_DURATION)
    except KeyboardInterrupt:
        print("\n[!] Interruption clavier détectée")
    
    print("\n" + "=" * 50)
    print("  DESKTOPOOP - Troll terminé !")
    print("=" * 50)
    
    # Nettoyage : supprimer les faux fichiers créés (DÉSACTIVÉ)
    # print("[*] Nettoyage des faux fichiers...")
    # delete_fake_icons()
    
    print("[*] Au revoir !")


if __name__ == "__main__":
    main()
