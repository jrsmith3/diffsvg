"""
Library functions for diffsvg.
"""

import xml.etree.ElementTree as ET

def common_node_ids(a, b):
    """
    Return list of nodes which are common between two SVG documents by id attribute.

    :param str a: String containing filename of first SVG document.
    :param str b: String containing filename of second SVG document.
    """
    ids_a = set([ el.attrib['id'] for el in a.iter() ])
    ids_b = set([ el.attrib['id'] for el in b.iter() ])

    return ids_a & ids_b

def extra_node_ids(a, b):
    """
    Return list of nodes in a which aren't in b by id attribute.

    :param str a: String containing filename of first SVG document.
    :param str b: String containing filename of second SVG document.
    """
    ids_a = set([ el.attrib['id'] for el in a.iter() ])
    ids_b = set([ el.attrib['id'] for el in b.iter() ])

    return ids_a - ids_b

def node_compare(a, b):
    """
    Return list of attribute names which differ between two SVG nodes.

    There are at least two ways of thinking of what's happening here. First, Does a contain keys that aren't found in b (or vice-versa). Second, of the common keys, which attributes are different?

    :param ElementTree.Element a: First SVG element.
    :param ElementTree.Element b: Second SVG element.
    """
    pass
