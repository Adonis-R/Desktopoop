import os
import random
import time
import ctypes
from pathlib import Path

try:
    import win32gui
    import win32con
    import win32api
    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False

from config import FAKE_FILE_NAMES


def get_desktop_path():
    """Récupère le chemin du bureau de l'utilisateur"""
    return Path(os.path.join(os.environ['USERPROFILE'], 'Desktop'))


def create_fake_icons():
    """Crée des faux fichiers sur le bureau"""
    desktop = get_desktop_path()
    created_files = []
    
    for name in FAKE_FILE_NAMES:
        fake_file = desktop / name
        try:
            # Créer un fichier vide
            fake_file.touch()
            created_files.append(str(fake_file))
        except Exception as e:
            print(f"Erreur création {name}: {e}")
    
    return created_files


def delete_fake_icons():
    """Supprime les faux fichiers créés"""
    desktop = get_desktop_path()
    
    for name in FAKE_FILE_NAMES:
        fake_file = desktop / name
        try:
            if fake_file.exists():
                fake_file.unlink()
        except Exception as e:
            print(f"Erreur suppression {name}: {e}")


def get_desktop_window():
    """Récupère le handle de la fenêtre du bureau (liste des icônes)"""
    if not HAS_WIN32:
        return None
    
    def callback(hwnd, result):
        class_name = win32gui.GetClassName(hwnd)
        if class_name == "SysListView32":
            result.append(hwnd)
        return True
    
    # Trouver la fenêtre Progman (bureau)
    progman = win32gui.FindWindow("Progman", None)
    
    # Trouver le WorkerW
    def_view = win32gui.FindWindowEx(progman, 0, "SHELLDLL_DefView", None)
    
    if not def_view:
        # Parfois le bureau est dans un WorkerW
        def enum_windows(hwnd, result):
            if win32gui.GetClassName(hwnd) == "WorkerW":
                child = win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None)
                if child:
                    result.append(hwnd)
            return True
        
        workers = []
        win32gui.EnumWindows(enum_windows, workers)
        if workers:
            def_view = win32gui.FindWindowEx(workers[0], 0, "SHELLDLL_DefView", None)
    
    if def_view:
        list_view = win32gui.FindWindowEx(def_view, 0, "SysListView32", None)
        return list_view
    
    return None


def get_icon_count():
    """Compte le nombre d'icônes sur le bureau"""
    if not HAS_WIN32:
        return 0
    
    list_view = get_desktop_window()
    if list_view:
        # LVM_GETITEMCOUNT = 0x1004
        count = win32api.SendMessage(list_view, 0x1004, 0, 0)
        return count
    return 0


def refresh_desktop():
    """Rafraîchit le bureau Windows"""
    if HAS_WIN32:
        # Envoie F5 au bureau
        shell = ctypes.windll.shell32
        shell.SHChangeNotify(0x8000000, 0x1000, None, None)


def move_icons():
    """Déplace les icônes du bureau de manière aléatoire (boucle)"""
    if not HAS_WIN32:
        print("pywin32 non disponible, impossible de déplacer les icônes")
        return
    
    while True:
        # Créer un faux fichier de temps en temps
        if random.random() < 0.3:  # 30% de chance
            create_fake_icons()
        
        refresh_desktop()
        time.sleep(random.randint(5, 10))


def hide_desktop_icons():
    """Cache toutes les icônes du bureau"""
    if not HAS_WIN32:
        return
    
    progman = win32gui.FindWindow("Progman", None)
    
    def enum_windows(hwnd, _):
        if win32gui.GetClassName(hwnd) == "WorkerW":
            child = win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None)
            if child:
                win32gui.ShowWindow(child, win32con.SW_HIDE)
        return True
    
    win32gui.EnumWindows(enum_windows, None)


def show_desktop_icons():
    """Réaffiche les icônes du bureau"""
    if not HAS_WIN32:
        return
    
    progman = win32gui.FindWindow("Progman", None)
    
    def enum_windows(hwnd, _):
        if win32gui.GetClassName(hwnd) == "WorkerW":
            child = win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None)
            if child:
                win32gui.ShowWindow(child, win32con.SW_SHOW)
        return True
    
    win32gui.EnumWindows(enum_windows, None)
