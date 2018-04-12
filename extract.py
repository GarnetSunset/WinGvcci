import colorgram, os

App = os.getenv('AppData')
TranscodedPaper = (App + "\Microsoft\Windows\Themes\TranscodedWallpaper")

colors = colorgram.extract(TranscodedPaper, 7)

first_color = colors[0]
rgb1  = first_color.rgb
print(rgb1)

second_color = colors[1]
rgb2  = second_color.rgb
print(rgb2)

third_color = colors[2]
rgb3  = third_color.rgb
print(rgb3)

fourth_color = colors[3]
rgb4  = fourth_color.rgb
print(rgb4)

fifth_color = colors[4]
rgb5  = fifth_color.rgb
print(rgb5)

sixth_color = colors[5]
rgb6  = sixth_color.rgb
print(rgb6)

seventh_color = colors[6]
rgb7  = seventh_color.rgb
print(rgb7)
