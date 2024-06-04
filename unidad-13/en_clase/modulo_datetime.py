


import datetime

# Fecha hora actual
ahora = datetime.datetime.now()

print(ahora.time())

if (ahora.hour < 12):
    print("Buenos días")
elif (ahora.hour < 18):
    print("Buenas tardes")
else:
    print("Buenas noches")

