import os

fileNames = [
    "S1-ADL1",
    "S1-ADL2",
    "S1-ADL3",
    "S1-ADL4",
    "S1-ADL5",
    "S1-Drill",
    "S2-ADL1",
    "S2-ADL2",
    "S2-ADL3",
    "S2-ADL4",
    "S2-ADL5",
    "S2-Drill",
    "S3-ADL1",
    "S3-ADL2",
    "S3-ADL3",
    "S3-ADL4",
    "S3-ADL5",
    "S3-Drill",
    "S4-ADL1",
    "S4-ADL2",
    "S4-ADL3",
    "S4-ADL4",
    "S4-ADL5",
    "S4-Drill"
]

with open("metadata.json", 'r') as file:
    metadataText = file.read()

for fileName in fileNames:
    os.mkdir(fileName)
    with open(os.path.join(fileName, "metadata.json"), 'w') as metaFile:
        metaFile.write(metadataText.replace("DISPLAYTARGET", fileName))
    with open(fileName + ".dat", 'r') as original_f:
        with open(os.path.join(fileName, "quaternion_data.dat"), 'w') as new_f:
            new_f.write(original_f.read())

