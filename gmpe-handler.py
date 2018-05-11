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
def createXML(ltId, ltlist, toOutput):
    root = Element("nrml")
    tree = ElementTree(root)
    root.set("xmlns:gml", "http://www.opengis.net/gml")
    root.set("xmlns", "http://openquake.org/xmlns/nrml/0.4")
    root2 = ET.SubElement(root, "logicTree", {"logicTreeID": ltId})
    print("###################")
    ltamt = len(ltlist)
    #print(ltamt)
    global usingCmd
    for x in range(0,ltamt):
        x = x+1
        if usingCmd == True: #When you decode a JSON, interger keys turn into strings. So, when we loop, we have to turn the loop number into a string
            x = str(x)
        specAt = ltlist[x] #specific attributes
        bsData = specAt["bsData"][x]
        ltBranchLevel = ET.SubElement(root2, "logicTreeBranchingLevel", {"branchingLevelID": specAt['branchingLevelID']})
        ltBranchSet = ET.SubElement(ltBranchLevel, "logicTreeBranchSet", {
            "uncertaintyType": "gmpeModel",
            "branchSetID": bsData["branchSetID"],
            "applyToTectonicRegionType": bsData["applyToTectonicRegionType"]
        })
        print("###################")
        bramt = len(specAt["ltBranch"][x])
        print(bramt)
        for z in range(0,bramt): #create branches
            z = z+1
            if usingCmd == True: #When you decode a JSON, interger keys turn into strings. So, when we loop, we have to turn the loop number into a string
                z = str(z)
            specAt2 = specAt["ltBranch"][x][z]
            ltBranch1 = ET.SubElement(ltBranchSet, "logicTreeBranch", {"branchSetID": specAt2["branchSetID"]})
            uncertaintyModel = ET.SubElement(ltBranch1, "uncertaintyModel", {"gmpe_table": specAt2["gmpe_table"]})
            uncertaintyModel.text = "GMPETable"
            uncertaintyWeight2 = ET.SubElement(ltBranch1, "uncertaintyWeight", {})
            print(specAt2["uncertaintyWeight"])
            uncertaintyWeight2.text = specAt2["uncertaintyWeight"]

    print(ET.tostring(root))
    tree.write(open(toOutput, 'w'), encoding='unicode',xml_declaration=True)

##########
# Actual ltData
##########
#get bsData from command line
usingCmd = True
#get ltData from command line
toOutput = "output_file.xml"
usingSpecOut = False
if len(args)>0:
    ltData1 = json.loads(args['-ltd'])
    if args['-output']:
        usingSpecOut = True
        toOutput = args['-output']
    print(ltData1)
else:
    usingCmd = False
    ltData1 = None
    print("ltData1 does not exist, using preset.")



##########
# End
##########
bsData = { #Default bsData
    1: {
        "branchSetID": "bs1",
        "applyToTectonicRegionType": "Active Shallow Fault",
    },
    2: {
        "branchSetID": "bs2",
        "applyToTectonicRegionType": "Subduction Interface",
    }
}
ltBranch = { #Default ltBranch
    1: {
        1: {
            "branchSetID": "b11",
            "text": "GMPETable",
            "gmpe_table": "../gm_tables/WcrustFRjb_low_clC.hdf5",
            "uncertaintyWeight": "0.2"
        },
        2: {
            "branchSetID": "b12",
            "text": "GMPETable",
            "gmpe_table": "../gm_tables/WcrustFRjb_low_clC.hdf5",
            "uncertaintyWeight": "0.8"
        }
    },
    2: {
        1: {
            "branchSetID": "b21",
            "text": "GMPETable",
            "gmpe_table": "../gm_tables/WcrustFRjb_low_clC.hdf5",
            "uncertaintyWeight": "0.2"
        }
    }
}
ltData = { #Default ltData
    1: {
        "branchingLevelID": "bl1",
        "ltBranch": ltBranch,
        "bsData": bsData
    },
    2: {
        "branchingLevelID": "bl2",
        "ltBranch": ltBranch,
        "bsData": bsData
    }
}
#print(ltData)
if usingCmd == True:
    #find out how many lists and branches there are...
    print(toOutput)
    createXML("lt1", ltData1, toOutput)
else:
    createXML("lt1", ltData, toOutput)
