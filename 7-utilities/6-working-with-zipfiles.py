from pathlib import Path
from zipfile import ZipFile

def createZip():
    zip=ZipFile("files.zip","w")
    path=Path("../ecommerce")
    for p in path.iterdir():
        zip.write(p)

# ________________________________________________
def extractZip():
    with ZipFile("files.zip") as zip:
        print(zip.namelist())
        zip.extractall("extracted files")

# createZip()

extractZip()

