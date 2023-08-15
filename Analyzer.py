from ultralytics import YOLO

import InteractionByCombination
import InteractionByDistance


class Analyzer:

    """
    das analyzemanagement dient dazu, detectobjects den dateipfad der zu analysierenden Datei zu übergeben.
    Anschließend wird je nach gewünschtem "Analysemodus" anhand der detektierten Objekte die Interaktionen erkannt
    das/die gewünschte/n Ergebnis/se werden dann an die main zurückgegeben.
    """
    def analyzemanagement(path, modus):
        result = Analyzer.detectObjects(path)
        if modus == 1:
            combination = InteractionByCombination.detectInteraction(result)
            return combination
        elif modus == 2:
            distance = InteractionByDistance.detectInteraction(result)
            return distance
        if modus == 0:
            combination = InteractionByCombination.detectInteraction(result)
            distance = InteractionByDistance.detectInteraction(result)
        return combination, distance

    """
    das analyzemanagement dient dazu, detectobjects den dateipfad der zu analysierenden Datei zu übergeben.
    Anschließend wird je nach gewünschtem "Analysemodus" anhand der detektierten Objekte die Interaktionen erkannt
    das/die gewünschte/n Ergebnis/se werden dann an die main zurückgegeben.
    """
    def detectObjects(path):
        # load pre-trained model
        model = YOLO("runs/detect/train8/weights/last.pt")
        # predict on an image
        detection_output = model.predict(source=path, conf=0.5, save=True, verbose=False)
        return detection_output
