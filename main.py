teilnehmer = ["Ben", "Mohammed", "Paul", "Klaus"]
punkte = input("Geben Sie die Punkte der Teilnehmer ein (getrennt durch Kommas): ").split(",")
punkte = [int(p.strip()) for p in punkte]  # Konvertiere den Input mit der .strip Funktion in eine Liste von Ganzzahlen
for i in range(len(teilnehmer)):
    print(teilnehmer[i], "ist Teilnehmer des Wettbewerbes.", "und hat", punkte[i], "Punkte erreicht.")