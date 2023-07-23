from Interaction import interactionCreator
from Videoobjects import videoobjectCreator


def find(tensor, value):
    """
    Sucht im Tensor nach Value, und gibt die Indizes der Gefundenen zurück.
    Wichtig, "find" erhält mit results[x].boxes.cls schon nur einen Tensor mit den detektieren Klassen in Frame x
    :param tensor:
    :param value:
    :return:
    """
    return (tensor == value).nonzero().tolist()


def contains(tensor, value):
    """
    Überprüft ob im tensor der gesuchte value vorhanden ist. Ja = True, Nein = False
    Durch results[x].boxes.cls erhält contains einen Tensor, der nur die Klassen der detektierten Objekte
    in Frame Nummer x enthält.
    :param tensor:
    :param value:
    :return:
    """
    return (tensor == value).any()


def checkDistance(tensor1, tensor2):
    """
    Überprüft anhand der Eckpunkte, ob sich die bounding boxes überlappen oder nicht.
    wenn ja = True, wenn nein = False als return
    :param tensor1:
    :param tensor2:
    :return:
    """
    x1_A, y1_A, x2_A, y2_A = tensor1[0]
    x1_B, y1_B, x2_B, y2_B = tensor2[0]
    # not negiert das ergebnis in der klammer.
    overlap = not (x1_A > x2_B or x2_A < x1_B or y1_A > y2_B or y2_A < y1_B)
    return overlap


def detectInteraction(results):
    """
    Es wird durch jeden Frame gegangen und geschaut ob mind. 1 Person (cls = 0) und mind. 1 Chipsschüssel (cls = 2)
    vorhanden ist. Anschließend wird für jede Kombination geprüft, ob die Bounding boxes sich überlappen
    Die Anzahl der Überlappungen wird in relevant persons gespeichert und dann in folgeframes auf veränderung
    geprüft. Verändert sich die Anzahl wird die Interaktion beendet und gespeichert
    In der Folgerunde der Iteration wird mit der neuen Anzahl Überlappungen eine Interaktion "gestartet"
    :param results:
    :return:
    """
    interactionList = []
    it = iter(range(len(results)))
    for x in it:
        # prüft ob überhaupt mind. 1 person & 1 chipsbowl zu sehen sind
        if contains(results[x].boxes.cls, 0) and contains(results[x].boxes.cls, 2):
            start = x
            interactiondetected = False
            a = find(results[x].boxes.cls, 0)
            b = find(results[x].boxes.cls, 2)
            typ = 1
            objectList = []
            relevantpersons = 0
            for index in range(len(b)):
                relevantbowl = False
                for y in range(len(a)):
                    # Überprüft überlappung der boundigboxen
                    if checkDistance(results[x].boxes.xyxy[b[index]], results[x].boxes.xyxy[a[y]]):
                        relevantbowl = True
                        interactiondetected = True
                        relevantpersons = relevantpersons + 1
                        video_objekt = videoobjectCreator(typ, "person",
                                                          *results[x].boxes.xywh[a[y]].tolist()[0],
                                                          results[x].boxes.conf[a[y]].item())
                        objectList.append(video_objekt)
                        typ = typ + 1
                if relevantbowl:
                    video_objekt = videoobjectCreator(typ, "chipsbowl",
                                                      *results[x].boxes.xywh[b[index]].tolist()[0],
                                                      results[x].boxes.conf[b[index]].item())
                    objectList.append(video_objekt)
                    typ = typ + 1
            interactingpersons = relevantpersons
            # überprüft ob sich die anzahl der überlappenden personen mit schüsseln verändert hat
            while interactingpersons == relevantpersons and x < len(results) - 1:
                relevantpersons = 0
                a = find(results[x].boxes.cls, 0)
                b = find(results[x].boxes.cls, 2)
                for index in range(len(b)):
                    for y in range(len(a)):
                        if checkDistance(results[x].boxes.xyxy[b[index]], results[x].boxes.xyxy[a[y]]):
                            relevantpersons = relevantpersons + 1
                x = next(it)
            end = x
            if interactiondetected:
                interaction = interactionCreator("A6", "eating chips", start, end, objectList)
                interactionList.append(interaction)
    print("Interaction by Distance durchgeführt")
    return interactionList
