import json
bsData = [
    {
        "branchSetID": "bs1",
        "applyToTectonicRegionType": "Active Shallow Fault",
    },
    {
        "branchSetID": "bs2",
        "applyToTectonicRegionType": "Subduction Interface",
    }
]
ltBranch = [
    [
        {
            "branchSetID": "b11",
            "text": "GMPETable",
            "gmpe_table": "../gm_tables/WcrustFRjb_low_clC.hdf5",
            "uncertaintyWeight": "0.2"
        }
    ]
]
ltBranch2 = [
    [
        {
            "branchSetID": "b21",
            "text": "GMPETable",
            "gmpe_table": "../gm_tables/WinterfaceCombo_lowclC.hdf5",
            "uncertaintyWeight": "0.2"
        }
    ]
]
ltData = [
    {
        "branchingLevelID": "bl1",
        "ltBranch": ltBranch,
        "bsData": bsData
    },
    {
        "branchingLevelID": "bl2",
        "ltBranch": ltBranch2,
        "bsData": bsData
    }
]






#json decode code (old):
if args['-bsdata']:
    bsData1 = args['-bsdata']
else:
    usingCmd = False
    bsData1 = None
    print("bsData1 does not exist, using preset.")
#get bsData from command line
if args['-ltbranch']:
    ltBranch1 = args['-ltbranch']
else:
    usingCmd = False
    ltBranch1 = None
    print("ltBranch1 does not exist, using preset.")










newBsData = json.loads(bsData, ensure_ascii=False)
#newLtData = json.dumps(ltData, ensure_ascii=False)
#newLtBranch = json.dumps(ltBranch, ensure_ascii=False)
print(newBsData)
#print(newLtData)
#print(newLtBranch)
