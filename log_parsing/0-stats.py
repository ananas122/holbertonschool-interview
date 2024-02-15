#!/usr/bin/python3
"""Script to get stats from a request"""

import sys

codes = {}
size = 0
count = 0  # Initialisation de la variable count

try:
    for ln in sys.stdin:
        parts = ln.split()
        if len(parts) > 2 and parts[-2].isdigit():
            size += int(parts[-1])
            code = parts[-2]
            if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                codes[code] = codes.get(code, 0) + 1

        count += 1
        if count % 10 == 0:  # Après chaque 10 lignes, imprimez les statistiques
            print("File size: {}".format(size))
            for key in sorted(codes.keys()):
                print("{}: {}".format(key, codes[key]))

except KeyboardInterrupt:
    # Imprimez les statistiques en cas d'interruption
    print("File size: {}".format(size))
    for key in sorted(codes.keys()):
        print("{}: {}".format(key, codes[key]))
    raise

# Imprimez les statistiques après avoir lu toutes les lignes
print("File size: {}".format(size))
for key in sorted(codes.keys()):
    print("{}: {}".format(key, codes[key]))
