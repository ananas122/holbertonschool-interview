#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    # Initialise le nombre d'octets de continuation attendus à 0
    nb_octets_restants = 0

    for nombre in data:
        # Vérifie que le nombre est un octet valide (entre 0 et 255)
        if nombre < 0 or nombre > 255:
            return False  # Si non valide, retourne False immédiatement

        if nb_octets_restants == 0:
            # Détermine le nombre d'octets de continuation attendus basé sur les bits de tête de l'octet actuel
            if (nombre >> 5) == 0b110:
                nb_octets_restants = 1  # Préfixe '110' indique 1 octet de continuation suivant
            elif (nombre >> 4) == 0b1110:
                nb_octets_restants = 2  # Préfixe '1110' indique 2 octets de continuation suivants
            elif (nombre >> 3) == 0b11110:
                nb_octets_restants = 3  # Préfixe '11110' indique 3 octets de continuation suivants
            elif (nombre >> 7):
                return False  # Si l'octet commence par '1', mais ne correspond à aucun cas ci-dessus, c'est invalide
        else:
            # Pour les octets de continuation, vérifie qu'ils commencent par '10'
            if (nombre >> 6) != 0b10:
                return False  # Si l'octet de continuation ne commence pas par '10', c'est invalide
            nb_octets_restants -= 1  # Décrémente le nombre d'octets de continuation attendus

    # Après avoir traité tous les octets, vérifie qu'il n'y a plus d'octets de continuation attendus
    return nb_octets_restants == 0
