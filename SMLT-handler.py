import configparser
import sys
import json
import os

#Notes:
# TO PASS PARAMETERS, USE JSON FORMAT!!




#ElementTree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET

##########
# Setup
##########

parser = configparser.SafeConfigParser()


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts
args = getopts(sys.argv)

##########
# Main
##########
def createXML(ltId, ltlist):
    root = Element("nrml")
    root.set("xmlns:gml", "http://www.opengis.net/gml")
    root.set("xmlns", "http://openquake.org/xmlns/nrml/0.4")
    root2 = ET.SubElement(root, "logicTree", {"logicTreeID": ltId})
    print("###################")
    ltamt = len(ltlist)
    print(ltamt)
    for x in range(0,ltamt):
        specAt = ltlist[x] #specific attributes
        bsData = specAt["bsData"][x]
        ltBranchLevel = ET.SubElement(root2, "logicTreeBranchingLevel", {"branchingLevelID": specAt['branchingLevelID']})
        ltBranchSet = ET.SubElement(ltBranchLevel, "logicTreeBranchSet", {
            "uncertaintyType": "sourceModel",
            "branchSetID": bsData["branchSetID"]
        })
        print("###################")
        bramt = len(specAt["ltBranch"][x-1])
        print(bramt)
        for z in range(0,bramt): #create branches
            specAt2 = specAt["ltBranch"][x-1][z-1]
            ltBranch1 = ET.SubElement(ltBranchSet, "logicTreeBranch", {"branchSetID": specAt2["branchSetID"]})
            uncertaintyModel = ET.SubElement(ltBranch1, "uncertaintyModel", {})
            uncertaintyModel.text = specAt2["uncertaintyModel"]
            uncertaintyWeight2 = ET.SubElement(ltBranch1, "uncertaintyWeight", {})
            uncertaintyWeight2.text = specAt2["uncertaintyWeight"]

    print(ET.tostring(root))

##########
# Actual ltData
##########
#get bsData from command line
usingCmd = True
#get ltData from command line
print("###################")
if len(args) == 0:
    usingCmd = False
    ltData1 = None
    print("ltData1 does not exist, using preset.")
else:
    ltData1 = json.loads(args['-ltd'])
    print(ltData1)



##########
# End
##########
bsData = [ #Default bsData
    {
        "branchSetID": "bs1"
    }
]
ltBranch = [ #Default ltBranch
    [
        {
            "branchSetID": "b1",
            "uncertaintyModel": "../../../sources/collapsed/eastern_arctic/EasternActic_H_Model_collapsed_rates.xml",
            "uncertaintyWeight": "0.2"
        }
    ]
]
ltData = [ #Default ltData
    {
        "branchingLevelID": "bl1",
        "ltBranch": ltBranch,
        "bsData": bsData
    }
]
#print(ltData)

if usingCmd == True:
    #find out how many lists and branches there are...
    createXML("lt1", ltData1)
else:
    createXML("lt1", ltData)
