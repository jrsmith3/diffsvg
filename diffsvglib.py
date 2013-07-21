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

def get_node_by_id(et_root, uid):
    """
    Return the node given an id.

    Returns None if the uid is not found in the SVG.

    :param xml.etree.ElementTree.Element et_root: SVG document in which to search.
    :param str uid: Unique identifier of an SVG node.
    """
    if et_root.attrib["id"] == uid:
        return et_root

    nodes = et_root.findall(".//*[@id='{0}']".format(uid))

    if len(nodes) == 0:
        return None
    elif len(nodes) == 1:
        return nodes[0]
    else:
        raise RuntimeError("Duplicate node id found: {0}.".format(uid))

def get_parent_node_by_id(et_root, uid):
    """
    Given an id, return the parent node. Return None if there's no parent.

    :param xml.etree.ElementTree.Element et_root: SVG document in which to search.
    :param str uid: Unique identifier of an SVG node.
    """
    if et_root.attrib["id"] == uid:
        return None

    nodes = et_root.findall(".//*[@id='{0}']..".format(uid))

    if len(nodes) == 0:
        raise RuntimeError("No node with id {0} found.".format(uid))
    elif len(nodes) == 1:
        return nodes[0]
    else:
        raise RuntimeError("Duplicate node id found: {0}.".format(uid))

