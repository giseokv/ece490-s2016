import json
from pprint import pprint

class jsonHandler(object):
    def __init__(self):
        self.bin_list = ["bin_A", "bin_B", "bin_C", "bin_D", "bin_E",    "bin_F","bin_G", "bin_H", "bin_I", "bin_J", "bin_K", "bin_L"]

    # Parses the input filename, and returns a tuple of the inital shelf mapping (bin name maps to bin contents) and the workOrder (all of the items in the tote)
    def readInFile(self, filename):
        with open(filename) as data_file:
            data = json.load(data_file)

        binMap = dict()
        workOrder = []

        for binName in self.bin_list:
            bin_contents = data["bin_contents"][binName]
            binMap[binName] = bin_contents

        workOrder = data["work_order"]

        return (binMap, workOrder)

    # Takes in the new shelfMap (the original map plus the added contents), and the final tote contents (ideally empty), and writes the output JSON file in the defined format
    def writeOutFile(self, filename, shelfMap, toteContents):

        with open(filename, "w") as file:
            json.dump({"bin_contents":{self.bin_list[i]:shelfMap[self.bin_list[i]] for i in range(0, len(self.bin_list))}, "work_order":toteContents}, file, indent=4, sort_keys=True)
