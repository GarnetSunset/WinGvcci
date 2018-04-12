import colorgram, os
import xml.etree.ElementTree as ET

counter = 1

WinGvcciXml = ET.parse('schemes\WinGvcci.itermcolors')  
root = WinGvcciXml.getroot()

App = os.getenv('AppData')
TranscodedPaper = (App + "\Microsoft\Windows\Themes\TranscodedWallpaper")

colors = colorgram.extract(TranscodedPaper, 7)

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
    if(counter == 49):
        elem.text = str(red1)
    if(counter == 50):
        elem.text = str(green1)
    if(counter == 51):
        elem.text = str(blue1)
    if(counter == 52):
        elem.text = str(red2)
    if(counter == 53):
        elem.text = str(green2)
    if(counter == 54):
        elem.text = str(blue2)
    if(counter == 55):
        elem.text = str(red3)
    if(counter == 56):
        elem.text = str(green3)
    if(counter == 57):
        elem.text = str(blue3)
    if(counter == 58):
        elem.text = str(red4)
    if(counter == 59):
        elem.text = str(green4)
    if(counter == 60):
        elem.text = str(blue4)
    if(counter == 61):
        elem.text = str(red5)
    if(counter == 62):
        elem.text = str(green5)
    if(counter == 63):
        elem.text = str(blue5)
    if(counter == 64):
        elem.text = str(red6)
    if(counter == 65):
        elem.text = str(green6)
    if(counter == 66):
        elem.text = str(blue6)
    if(counter == 67):
        elem.text = str(red7)
    if(counter == 68):
        elem.text = str(green7)
    if(counter == 69):
        elem.text = str(blue7)
    
    counter += 1

WinGvcciXml.write('schemes/WinGvcci.itermcolors')

os.system("colortool -q -b WinGvcci")
