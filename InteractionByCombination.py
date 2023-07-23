from Interaction import interactionCreator
from Videoobjects import videoobjectCreator


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


def find(tensor, value):
    """
    Sucht im Tensor nach Value, und gibt die Indizes der Gefundenen zurück.
    Wichtig, "find" erhält mit results[x].boxes.cls schon nur einen Tensor mit den detektieren Klassen in Frame x
    :param tensor:
    :param value:
    :return:
    """
    return (tensor == value).nonzero().tolist()


def detectInteraction(results):
    """
    prüft pro Frame ob eating_animation(cls = 1) UND chipsschüssel(cls = 2) erkannt werden
    Nein? Nächster Frame. Ja? Solange das auf den aktuellen Frame zutrifft, prüfe für den nächsten.
    Wird im nächsten nicht beides detektiert, dann ist aktuelles x = end und Interaktion wird erstellt
    Schleife beginnt für den nächsten Frame von vorn, alle Interaktionen werden in eine Liste gespeichert (results)
    :param results:
    :return:
    """
    interactionList = []
    it = iter(range(len(results)))
    for x in it:
        # sind beide gesuchten objekte im Frame detektiert worden?
        if contains(results[x].boxes.cls, 1) and contains(results[x].boxes.cls, 2):
            start = x
            # Liste der Indizes an denen die jewaligen Objekte detektiert wurden
            a = find(results[x].boxes.cls, 1)
            b = find(results[x].boxes.cls, 2)
            typ = 1
            objectList = []
            for index in range(len(a)):
                # a[index] zeigt den index im tensor des aktuellen frames auf das gesuchte objekt
                video_objekt = videoobjectCreator(typ, "eating_animation",
                                                  *results[x].boxes.xywh[a[index]].tolist()[0],
                                                  results[x].boxes.conf[a[index]].item())
                objectList.append(video_objekt)
                typ = typ + 1
            for index in range(len(b)):
                video_objekt = videoobjectCreator(typ, "eating_animation",
                                                  *results[x].boxes.xywh[b[index]].tolist()[0],
                                                  results[x].boxes.conf[b[index]].item())
                objectList.append(video_objekt)
                typ = typ + 1
            while contains(results[x].boxes.cls, 1) and contains(results[x].boxes.cls, 2) and x < len(results) - 1:
                x = next(it)
            end = x
            # die interaktion wird mitsamt der objectList instanziiert
            interaction = interactionCreator("A6", "eating chips", start, end, objectList)
            interactionList.append(interaction)
    print("Interactions by Combination durchgeführt")
    return interactionList
