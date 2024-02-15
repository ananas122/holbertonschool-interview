#!/usr/bin/python3
"""Script to get stats from a request"""

import sys

codes = {}
size = 0

try:
    for ln in sys.stdin:
        parts = ln.split()
        # Validation de la ligne pour s'assurer qu'elle correspond au format attendu
        if len(parts) > 6 and parts[2] == '-' and 'GET' in parts[3] and parts[4].startswith('/projects/260') and parts[5].startswith('HTTP/1.1') and parts[6].isdigit() and parts[-1].isdigit():
            size += int(parts[-1])
            code = parts[6]
            if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                codes[code] = codes.get(code, 0) + 1

except KeyboardInterrupt:
    pass

# Imprimez les statistiques finales
print("File size: {}".format(size))
for key in sorted(codes.keys()):
    print("{}: {}".format(key, codes[key]))
