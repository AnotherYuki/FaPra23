import Analyzer
import XmlWriter
import os


def printlists(interactions):
    """
    printlists gibt alle Ergebnisse aus der Ergebnisliste der erkannten Interaktionen an den Nutzer aus
    Falls keine Interaktion erkannt wurde, wird der Nutzer informiert
    :param interactions:
    :return:
    """
    if len(interactions) == 0:
        print("Keine Interaktionen erkannt")
    else:
        for interaction in interactions:
            print(interaction)
            # for vobject in interaction.objects:
            #     print(vobject)


"""
Die main erfüllt die Aufgabe des modellierten "Prozessors" aus Kapitel 3
und ist für den Ablauf und die Abfrage der notwendigen informationen Zuständig
"""
dateipfad = input("Bitte geben Sie den Dateipfad für das zu untersuchende Video in die Kommandozeile ein:\n")
modus = input("Bitte wähle eine Analysevariante:\n0 - Beide Varianten\n"
              "1 - Erkennung anhand der Kombination\n2 - Erkennung anhand der Distanz\n")
modus = int(modus)
save = input("Soll das Ergebnis als .xml gespeichert werden? (ja/nein)\n")
Analyzer = Analyzer
if modus == 0:
    combination, distance = Analyzer.Analyzer.analyzemanagement(dateipfad, modus)
    print("Ergebnisse für Interaktionen nach Kombination:")
    printlists(combination)
    print("Ergebnisse für Interaktionen nach Distanz:")
    printlists(distance)
if modus == 1 or modus == 2:
    result = Analyzer.Analyzer.analyzemanagement(dateipfad, modus)
    print("Detektierte Interaktionen:")
    printlists(result)
if save == "ja":
    savein = input("Wohin soll die .xml gespeichert werden? Bitte gib einen Dateipfad ein\n")
    dateiname = os.path.basename(dateipfad)
    if modus == 0:
        XmlWriter.erstelle_xml(combination, dateiname, os.path.join(savein + "/combination.xml"))
        XmlWriter.erstelle_xml(distance, dateiname, os.path.join(savein + "/distance.xml"))
    if modus == 1:
        XmlWriter.erstelle_xml(result, dateiname, os.path.join(savein + "/combination.xml"))
    if modus == 2:
        XmlWriter.erstelle_xml(result, dateiname, os.path.join(savein + "/distance.xml"))
