# The point of this code is to pull all of the ids for all of the elements in A.svg and B.svg. At that point, we can determine if there are elements in A.svg that aren't in B.svg.

# Basically what's going to happen here is I'm going to create a set with all of the ids from both SVGs and do a set operation.

treeA = ElementTree.parse("A.svg")
treeB = ElementTree.parse("B.svg")

trA = treeA.getroot()
trB = treeB.getroot()

# Make some empty sets
aset = set()
bset = set()

for elem in trA.getiterator():
  aset.add(elem.attrib["id"])

for elem in trB.getiterator():
  bset.add(elem.attrib["id"])
  
print aset - bset