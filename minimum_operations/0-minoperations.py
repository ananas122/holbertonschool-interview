#!/usr/bin/python3
"""
Module which contains minoperations function
"""


def minOperations(n):
    operation_count = 0  # Nombre total d'opérations effectuées
    current_length = 1   # Longueur actuelle du texte dans le fichier
    copied_length = 0    # Longueur du texte qui a été copié

    while current_length < n:
        if n % current_length == 0:  # Copier quand var est un / de n
            copied_length = current_length
            current_length *= 2  # Coller après copie (double la longueur)
            operation_count += 1  # Opération de copie
        else:
            current_length += copied_length  # Coller le contenu copié
        # Opération de collage (toujours effectuée après copie ou directement)
        operation_count += 1

    return operation_count
