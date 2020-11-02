import xml.etree.ElementTree as ET


def get_xml_depth(xml):
    xml = ET.fromstring(xml)
    depth = 0
    for node in xml:
        d = 0
        for e in node.iter():
            d += 1
        depth = d if d > depth else depth
    return depth
