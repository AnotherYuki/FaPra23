import xml.etree.ElementTree as Xmlt
from datetime import datetime


def erstelle_xml(interaktionen, video_dateipfad, dateiname):
    root = Xmlt.Element('Interaktionen')

    # Füge den Dateipfad und das aktuelle Datum hinzu
    Xmlt.SubElement(root, 'file').text = video_dateipfad
    Xmlt.SubElement(root, 'date').text = datetime.now().strftime('%d-%m-%Y')

    for interaktion in interaktionen:
        interaktion_elem = Xmlt.SubElement(root, 'interaktion', attrib={'begin': str(interaktion.begin),
                                                                        'end': str(interaktion.end)})
        Xmlt.SubElement(interaktion_elem, 'type').text = interaktion.typ
        Xmlt.SubElement(interaktion_elem, 'descrption').text = interaktion.description

        for vobject in interaktion.objects:
            vobject_elem = Xmlt.SubElement(interaktion_elem, 'object')
            Xmlt.SubElement(vobject_elem, 'id').text = str(vobject.id)
            Xmlt.SubElement(vobject_elem, 'term').text = vobject.term
            bbox_elem = Xmlt.SubElement(vobject_elem, 'bounding-box')
            Xmlt.SubElement(bbox_elem, 'x').text = str(vobject.x)
            Xmlt.SubElement(bbox_elem, 'y').text = str(vobject.y)
            Xmlt.SubElement(bbox_elem, 'width').text = str(vobject.width)
            Xmlt.SubElement(bbox_elem, 'height').text = str(vobject.height)
            Xmlt.SubElement(vobject_elem, 'probability').text = str(vobject.probability)

    tree = Xmlt.ElementTree(root)
    with open(dateiname, 'wb') as file:
        tree.write(file)
        print("Xml gespeichert")
