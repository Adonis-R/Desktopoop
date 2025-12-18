import pyautogui
import random
import time

from config import MOUSE_SHAKE_INTENSITY, MOUSE_MOVE_INTERVAL

# Désactive le failsafe (normalement, bouger la souris en haut à gauche arrête pyautogui)
pyautogui.FAILSAFE = False


def get_screen_size():
    """Récupère la taille de l'écran"""
    return pyautogui.size()


def move_cursor_to_random_position():
    """Déplace la souris à une position aléatoire sur l'écran"""
    width, height = get_screen_size()
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))


def move_cursor_randomly():
    """Déplace la souris aléatoirement en boucle"""
    while True:
        move_cursor_to_random_position()
        wait_time = random.uniform(*MOUSE_MOVE_INTERVAL)
        time.sleep(wait_time)


def shake_cursor():
    """Fait trembler le curseur en boucle"""
    while True:
        x, y = pyautogui.position()
        offset_x = random.randint(-MOUSE_SHAKE_INTENSITY, MOUSE_SHAKE_INTENSITY)
        offset_y = random.randint(-MOUSE_SHAKE_INTENSITY, MOUSE_SHAKE_INTENSITY)
        
        # S'assurer de rester dans les limites de l'écran
        width, height = get_screen_size()
        new_x = max(0, min(width - 1, x + offset_x))
        new_y = max(0, min(height - 1, y + offset_y))
        
        pyautogui.moveTo(new_x, new_y)
        time.sleep(0.05)


def cursor_escape():
    """Le curseur s'enfuit quand on essaie de l'utiliser"""
    while True:
        x, y = pyautogui.position()
        # Petit déplacement aléatoire
        offset = random.randint(50, 150)
        direction_x = random.choice([-1, 1])
        direction_y = random.choice([-1, 1])
        
        width, height = get_screen_size()
        new_x = max(0, min(width - 1, x + (offset * direction_x)))
        new_y = max(0, min(height - 1, y + (offset * direction_y)))
        
        pyautogui.moveTo(new_x, new_y, duration=0.1)
        time.sleep(random.uniform(0.3, 0.8))


def invert_cursor_movement():
    """Inverse les mouvements de la souris (difficile à implémenter proprement)"""
    last_x, last_y = pyautogui.position()
    while True:
        current_x, current_y = pyautogui.position()
        
        # Calculer le delta
        delta_x = current_x - last_x
        delta_y = current_y - last_y
        
        if delta_x != 0 or delta_y != 0:
            # Inverser le mouvement
            width, height = get_screen_size()
            new_x = max(0, min(width - 1, current_x - (delta_x * 2)))
            new_y = max(0, min(height - 1, current_y - (delta_y * 2)))
            pyautogui.moveTo(new_x, new_y)
        
        last_x, last_y = current_x, current_y
        time.sleep(0.01)
