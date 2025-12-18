import webbrowser
import time
import random

from config import TROLL_URLS, BROWSER_OPEN_INTERVAL


def open_random_page():
    """Ouvre une page aléatoire dans le navigateur par défaut"""
    url = random.choice(TROLL_URLS)
    webbrowser.open(url)


def open_random_pages():
    """Ouvre des pages aléatoires périodiquement (boucle infinie)"""
    while True:
        open_random_page()
        wait_time = random.randint(*BROWSER_OPEN_INTERVAL)
        time.sleep(wait_time)


def open_multiple_tabs(count=5):
    """Ouvre plusieurs onglets d'un coup"""
    for _ in range(count):
        open_random_page()
        time.sleep(0.5)
