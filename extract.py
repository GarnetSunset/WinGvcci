import colorgram, os, shutil, zipfile
import xml.etree.ElementTree as ET
from PIL import Image
from resizeimage import resizeimage
from six.moves.urllib.request import urlopen
import winreg

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

if not os.path.isfile('colortool.exe'):
    os.rename("schemes","schemestemp")
    chromeDL = urlopen("https://github.com/Microsoft/console/releases/download/1708.14008/colortool.zip")
    with open(os.path.basename("https://github.com/Microsoft/console/releases/download/1708.14008/colortool.zip"), "wb") as local_file:
                local_file.write(chromeDL.read())
    zippy = zipfile.ZipFile("colortool.zip","r")
    zippy.extractall(owd)
    zippy.close()
    os.remove("colortool.zip")
    shutil.rmtree("schemes")
    os.rename("schemestemp","schemes")
    
WinGvcciXml = ET.parse('schemes\WinGvcci.itermcolors')  
root = WinGvcciXml.getroot()

REG_PATH = r"Control Panel\Desktop"

colors = colorgram.extract(get_reg('WallPaper'), 7)

fullList = []

for color in colors:
    counter = 2
    while counter != -1:
        fullList.append(str(float(color.rgb[counter])/255))
        counter = counter - 1

counter = 0

for elem in root.iter('real'):
    elem.text = fullList[counter]
    counter += 1
    if counter == 7:
        counter = 0

WinGvcciXml.write('schemes/WinGvcci.itermcolors')

os.system("colortool -q -b WinGvcci")
