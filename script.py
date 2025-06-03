#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
script.py

Script de démonstration pour l'entraînement aux commandes Git.
Auteur : valorisa
Date : 2025-06-03
"""

import sys

def afficher_bienvenue():
    """Affiche un message de bienvenue."""
    print("Bienvenue dans le script d'entraînement Git !")

def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

def soustraction(a, b):
    """Retourne la différence entre deux nombres."""
    return a - b

def main():
    """Point d'entrée du script."""
    afficher_bienvenue()
    print("Addition de 2 et 3 :", addition(2, 3))
    print("Soustraction de 5 et 2 :", soustraction(5, 2))

    # Exemple d'utilisation des arguments de la ligne de commande
    if len(sys.argv) > 2:
        try:
            x = float(sys.argv[1])
            y = float(sys.argv[2])
            print(f"Addition de {x} et {y} :", addition(x, y))
        except ValueError:
            print("Veuillez fournir deux nombres valides en arguments.")

if __name__ == "__main__":
    main()
