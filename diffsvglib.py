"""
Library functions for diffsvg.
"""

import xml.etree.ElementTree as ET

def common_node_ids(a, b):
    """
    Return list of nodes which are common between two SVG documents by id attribute.

    :param etree.ElementTree a: ElementTree representing first SVG document.
    :param etree.ElementTree a: ElementTree representing second SVG document.
    """
    ids_a = set([ el.attrib['id'] for el in a.iter() ])
    ids_b = set([ el.attrib['id'] for el in b.iter() ])

    return ids_a & ids_b

def extra_node_ids(a, b):
    """
    Return list of nodes in a which aren't in b by id attribute.

    :param etree.ElementTree a: ElementTree representing first SVG document.
    :param etree.ElementTree a: ElementTree representing second SVG document.
    """
    ids_a = set([ el.attrib['id'] for el in a.iter() ])
    ids_b = set([ el.attrib['id'] for el in b.iter() ])

    return ids_a - ids_b

def common_attrib_keys(a, b):
    """
    Return list of attributes which are common between two SVG elements by attribute key.

    :param xml.etree.ElementTree.Element a: First element
    :param xml.etree.ElementTree.Element b: Second element
    """
    return set(a.attrib.keys()) & set(b.attrib.keys())

def extra_attrib_keys(a, b):
    """
    Return list of attributes in a which aren't in b by attribute key.

    :param xml.etree.ElementTree.Element a: First element
    :param xml.etree.ElementTree.Element b: Second element
    """
    return set(a.attrib.keys()) - set(b.attrib.keys())

def node_compare(a, b):
    """
    Return list of attribute names which differ between two SVG nodes.

    There are at least two ways of thinking of what's happening here. First, Does a contain keys that aren't found in b (or vice-versa). Second, of the common keys, which attributes are different?

    :param ElementTree.Element a: First SVG element.
    :param ElementTree.Element b: Second SVG element.
    """
    pass
