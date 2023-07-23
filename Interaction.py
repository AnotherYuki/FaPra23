# interactionCreator ermöglicht es von außerhalb Objekte vom Typ Interaktion zu instanziieren.
def interactionCreator(typ, description, begin, end, objekte):
    newObj = Interaction(typ, description, begin, end, objekte)
    return newObj


class Interaction:
    """
    Die  Klasse Interaction enthält alle wichtigen Informationen über eine Interaktion
    typ (in unserem Fall A6 = Interaktion mit Objekten), description = beschreibung
    begin und end wird als startframe und endframe gespeichert, NICHT als zeitstempel
    objects enthält die Liste aller Objekte, die an der Interaktion beteiligt sind.
    """

    def __init__(self, typ, description, begin, end, detectedobjects):
        self.typ = typ
        self.description = description
        self.begin = begin
        self.end = end
        self.objects = detectedobjects

    # __str__ definiert, wie Objekte vom Typ Interaktion an den Nutzer ausgegeben werden sollen.
    def __str__(self):
        return f"interaction begin={self.begin} end={self.end}\n" \
               f"type {self.typ}\ndescription {self.description}"

    # print_values ruft die __str__ funktion von Videoobjects für jedes an Interaktion beteiligte Objekt auf.
    def print_values(self):
        for instance in self.objects:
            print(instance)
