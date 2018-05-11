import tkinter as tk
import os
import json
import sys

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

def sendGmpe():
    newData = json.dumps(json.dumps(ltData)) #Required double to do escape quotes...
    cmds = "python gmpe-handler.py -output specout.xml -ltd "+newData

    print(cmds)
    print("###################")
    print(newData)
    print("###################")
    print(json.loads(newData))
    os.system(cmds)
sendGmpe()
