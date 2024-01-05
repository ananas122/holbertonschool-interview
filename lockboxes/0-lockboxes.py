#!/usr/bin/python3
"""
Write a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
 """
    Determines if all the boxes can be unlocked using the provided keys.

    Args:
    - boxes: A list of lists. Each sublist represents a box containing keys
     to open other boxes.

    Returns:
    - True if all boxes can be unlocked, else False.
    """

 '''Check if the list is empty or null (no boxes to open)'''

    boxopen = {0}  # Commence avec la boîte 0 ouverte
    clés = boxes[0]  # Prend les clés de la première boîte

    while clés:
        new_clé = clés.pop()  # Prend une clé
        if new_clé not in boxopen and new_clé < len(boxes):
            # Ajoute la boîte à la liste des ouvertes
            boxopen.add(new_clé)
            clés.extend(boxes[new_clé])  # Ajoute les nouvelles clés

    return len(boxopen) == len(boxes)
