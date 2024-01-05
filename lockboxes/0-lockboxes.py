#!/usr/bin/python3
    """_summary_
    """

def canUnlockAll(boxes):
    boxopen = {0}  # Commence avec la boîte 0 ouverte
    clés = boxes[0]  # Prend les clés de la première boîte

    while clés:
        new_clé = clés.pop()  # Prend une clé
        if new_clé not in boxopen and new_clé < len(boxes):
            # Ajoute la boîte à la liste des ouvertes
            boxopen.add(new_clé)
            clés.extend(boxes[new_clé])  # Ajoute les nouvelles clés

    return len(boxopen) == len(boxes)
