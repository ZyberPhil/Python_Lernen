import time

# Startzeit ermitteln
start = time.time()

# Ausführen des Codeblocks, den wir messen wollen
print('Hallo Welt!')
time.sleep(0.2)

# Endzeit bestimmen
end = time.time()

# Berechnung der verstrichenen Zeit
verstrichene_zeit = end - start
time = round(verstrichene_zeit, 2)
print(f'Ausführungszeit: {verstrichene_zeit} Sekunden')