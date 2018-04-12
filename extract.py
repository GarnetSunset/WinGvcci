import colorgram, os
from xml.dom import minidom

mydoc = minidom.parse('schemes\WinGvcci.itermcolors')

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





