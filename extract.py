import colorgram, os, shutil, zipfile
import xml.etree.ElementTree as ET
from PIL import Image
from resizeimage import resizeimage
from six.moves.urllib.request import urlopen

counter = 1
owd = os.getcwd()

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
    
    
counter = 1

WinGvcciXml = ET.parse('schemes\WinGvcci.itermcolors')  
root = WinGvcciXml.getroot()

App = os.getenv('AppData')
if os.path.isfile(App + "\Microsoft\Windows\Themes\Transcoded_001"):
    TranscodedPaper = (App + "\Microsoft\Windows\Themes\Transcoded_001")
else:
    TranscodedPaper = (App + "\Microsoft\Windows\Themes\TranscodedWallpaper")
shutil.copyfile(TranscodedPaper, "Wallpapers/TranscodedPaper.jpg")
with open("Wallpapers/TranscodedPaper.jpg", 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [1200, 600])
        cover.save('Wallpapers/TranscodedPaperConvert.jpg', image.format)

colors = colorgram.extract('Wallpapers/TranscodedPaperConvert.jpg', 7)

first_color = colors[0]
rgb1  = first_color.rgb
red1 = float(rgb1.r)/255
green1 = float(rgb1.g)/255
blue1 = float(rgb1.b)/255

second_color = colors[1]
rgb2  = second_color.rgb
red2 = float(rgb2.r)/255
green2 = float(rgb2.g)/255
blue2 = float(rgb2.b)/255

third_color = colors[2]
rgb3  = third_color.rgb
red3 = float(rgb3.r)/255
green3 = float(rgb3.g)/255
blue3 = float(rgb3.b)/255

fourth_color = colors[3]
rgb4  = fourth_color.rgb
red4 = float(rgb4.r)/255
green4 = float(rgb4.g)/255
blue4 = float(rgb4.b)/255

fifth_color = colors[4]
rgb5  = fifth_color.rgb
red5 = float(rgb5.r)/255
green5 = float(rgb5.g)/255
blue5 = float(rgb5.b)/255

sixth_color = colors[5]
rgb6  = sixth_color.rgb
red6 = float(rgb6.r)/255
green6 = float(rgb6.g)/255
blue6 = float(rgb6.b)/255

seventh_color = colors[6]
rgb7  = seventh_color.rgb
red7 = float(rgb7.r)/255
green7 = float(rgb7.g)/255
blue7 = float(rgb7.b)/255

for elem in root.iter('real'):
    if(counter == 3):
        elem.text = str(red1)
    if(counter == 2):
        elem.text = str(green1)
    if(counter == 1):
        elem.text = str(blue1)
    if(counter == 6):
        elem.text = str(red2)
    if(counter == 5):
        elem.text = str(green2)
    if(counter == 4):
        elem.text = str(blue2)
    if(counter == 9):
        elem.text = str(red3)
    if(counter == 8):
        elem.text = str(green3)
    if(counter == 7):
        elem.text = str(blue3)
    if(counter == 10):
        elem.text = str(blue4)
    if(counter == 11):
        elem.text = str(green4)
    if(counter == 12):
        elem.text = str(red4)
    if(counter == 13):
        elem.text = str(blue5)
    if(counter == 14):
        elem.text = str(green5)
    if(counter == 15):
        elem.text = str(red5)
    if(counter == 16):
        elem.text = str(blue6)
    if(counter == 17):
        elem.text = str(green6)
    if(counter == 18):
        elem.text = str(red6)
    if(counter == 19):
        elem.text = str(blue7)
    if(counter == 20):
        elem.text = str(green7)
    if(counter == 21):
        elem.text = str(red7)
    if(counter == 22):
        elem.text = str(blue6)
    if(counter == 23):
        elem.text = str(green6)
    if(counter == 24):
        elem.text = str(red6)
    if(counter == 27):
        elem.text = str(red3)
    if(counter == 26):
        elem.text = str(green3)
    if(counter == 25):
        elem.text = str(blue3)
    if(counter == 28):
        elem.text = str(blue4)
    if(counter == 29):
        elem.text = str(green4)
    if(counter == 30):
        elem.text = str(red4)
    if(counter == 31):
        elem.text = str(blue5)
    if(counter == 32):
        elem.text = str(green5)
    if(counter == 33):
        elem.text = str(red5)
    if(counter == 34):
        elem.text = str(blue6)
    if(counter == 35):
        elem.text = str(green6)
    if(counter == 36):
        elem.text = str(red6)
    if(counter == 37):
        elem.text = str(blue4)
    if(counter == 38):
        elem.text = str(green4)
    if(counter == 39):
        elem.text = str(red4)
    if(counter == 40):
        elem.text = str(blue7)
    if(counter == 41):
        elem.text = str(green7)
    if(counter == 42):
        elem.text = str(red7)
    if(counter == 62):
        elem.text = str(blue7)
    if(counter == 63):
        elem.text = str(green7)
    if(counter == 64):
        elem.text = str(red7)
    
    counter += 1

WinGvcciXml.write('schemes/WinGvcci.itermcolors')

os.system("colortool -q -b WinGvcci")
