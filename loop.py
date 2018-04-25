import os, time  

App = os.getenv('AppData')
transcodedsize = 0

while(1 == 1):
    transcodedafter = os.path.getsize(App + "/Microsoft/Windows/Themes/TranscodedWallpaper")
    if(transcodedafter != transcodedsize):
        os.system("python extract.py")
    transcodedsize = os.path.getsize(App + "/Microsoft/Windows/Themes/TranscodedWallpaper")
    time.sleep(60)
