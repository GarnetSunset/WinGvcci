import colorgram, os, shutil, zipfile
import xml.etree.ElementTree as ET
from PIL import Image
from PIL import ImageFile
import winreg
import xmltodict

ImageFile.LOAD_TRUNCATED_IMAGES = True

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

counter = 1

if not os.path.exists("Wallpapers"):
    os.makedirs("Wallpapers")
    

with open('schemes\WinGvcci.itermcolors') as fd:
    doc = xmltodict.parse(fd.read())
WinGvcciXml = ET.parse('schemes\WinGvcci.itermcolors')  
root = WinGvcciXml.getroot()

REG_PATH = r"Control Panel\Desktop"

colors = colorgram.extract(get_reg('WallPaper'), 7)

fullList = []
dark = []
light = []

for color in colors:
    counter = 2
    while counter != -1:
        corrected = float(color.rgb[counter])/255
        fullList.append(str(corrected))
        counter = counter - 1
        if counter == -1:
            if color.rgb[0]+color.rgb[1]+color.rgb[2] > 382:
                light.append(color.rgb[0]+color.rgb[1]+color.rgb[2])
            else:
                dark.append(color.rgb[0]+color.rgb[1]+color.rgb[2])


if colors[0].rgb[0]+colors[0].rgb[1]+colors[0].rgb[2] in dark:
    firstColor = "dark"
else:
    firstColor = "light"

keys = len(root.findall("./dict/key"))

totalCount = 0
countColor = 0
for elem in root.iter('real'):
    elem.text = fullList[countColor]
    countColor += 1
    totalCount += 1
    if totalCount == 0 or totalCount == 1 or totalCount == 2:
        newNum = 1.0 - float(fullList[countColor])
        elem.text = str(newNum)
    if countColor == 7:
        countColor = 0

WinGvcciXml.write('schemes/WinGvcci.itermcolors')

os.system("colortool -q -b WinGvcci")
