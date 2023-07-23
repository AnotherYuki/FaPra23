class Videoobjects:
    """
    Videoobjects enthält alle Informationen/Attribute der Objekte.
    id enthält eine Nummer zur identifikation, die pro Interaktion nur einmalig vergeben wird (zählt von 1 aufwärts)
    term enthält die information um was für ein objekt es sich  handelt
    x, y, width und height beinhalten die boundingbox im vom Yolo genutzten Format (x,y = zentrum)
    probability enthält die "confidence" mit der yolo das objekt detektiert hat.
    """
    def __init__(self, number, term, x, y, width, height, probability):
        self.id = number
        self.term = term
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.probability = probability

    # __str__ definiert wie videoobjects an den Nutzer ausgegeben werden sollen.
    def __str__(self):
        return f"object\nid {self.id}\nterm {self.term}\n" \
               f"bounding box \nx {self.x}\ny {self.y}\nwidth {self.width}\nheight {self.height}\n" \
               f"probability {self.probability}"


# videoobjectCreator ermöglicht das Instanziieren von Videoobjects von außerhalb
def videoobjectCreator(number, term1, xcor, ycor, width, height, probability):
    newObj = Videoobjects(number, term1, xcor, ycor, width, height, probability)
    return newObj
