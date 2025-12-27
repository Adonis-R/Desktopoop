"""
Desktopoop - Rickroll + Curseur Troll
=====================================

Pour arrêter : CTRL+SHIFT+ESC -> Fin de tâche "TrollApp.exe"
"""

import webbrowser
import time
import ctypes
import sys
import os

# Configuration
RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
RICKROLL_INTERVAL = 30  # secondes entre chaque rickroll
TROLL_DURATION = 20    # durée totale en secondes


def get_asset_path(filename):
    """Retourne le chemin vers un fichier dans assets (compatible .exe)"""
    if getattr(sys, 'frozen', False):
        # Si compilé en .exe
        base_path = sys._MEIPASS
    else:
        # Si exécuté en Python
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "assets", filename)


def change_cursor():
    """Change le curseur système avec cursor.cur"""
    try:
        cursor_path = get_asset_path("cursor.cur")
        if os.path.exists(cursor_path):
            # Charger le curseur personnalisé
            cursor_handle = ctypes.windll.user32.LoadCursorFromFileW(cursor_path)
            # Appliquer à tous les types de curseurs
            cursors = [32512, 32513, 32514, 32515, 32516, 32642, 32643, 32644, 32645, 32646, 32648, 32649, 32650, 32651]
            for cursor_id in cursors:
                ctypes.windll.user32.SetSystemCursor(cursor_handle, cursor_id)
            print("[+] Curseur modifié !")
            return True
    except Exception as e:
        print(f"[-] Erreur curseur: {e}")
    return False


def restore_cursors():
    """Restaure les curseurs par défaut"""
    try:
        ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0)
        print("[+] Curseurs restaurés")
    except Exception as e:
        print(f"[-] Erreur restauration: {e}")


def open_rickroll():
    """Ouvre un rickroll"""
    webbrowser.open(RICKROLL_URL)
    print("[+] Rickroll envoyé !")


def main():
    print("=" * 40)
    print("  DESKTOPOOP - Troll activé !")
    print(f"  Durée : {TROLL_DURATION} secondes")
    print("=" * 40)
    
    # Changer le curseur
    change_cursor()
    
    # Ouvrir des rickrolls périodiquement
    start_time = time.time()
    open_rickroll()  # Premier rickroll immédiat
    
    try:
        while time.time() - start_time < TROLL_DURATION:
            time.sleep(RICKROLL_INTERVAL)
            if time.time() - start_time < TROLL_DURATION:
                open_rickroll()
    except KeyboardInterrupt:
        print("\n[!] Interruption")
    
    # Restaurer les curseurs
    restore_cursors()
    
    print("=" * 40)
    print("  DESKTOPOOP - Terminé !")
    print("=" * 40)


if __name__ == "__main__":
    main()
