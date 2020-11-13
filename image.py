from PIL import Image, ImageDraw, ImageFont
import os
import glob
import sys
from copy import deepcopy

def digs2(m):
    out = '00'[len(str(m)):] + str(m)
    return out
#https://stackoverflow.com/questions/134934/display-number-with-leading-zeros

korrMin = -5
intervall = 6


path = "pics/"
for CleanUp in glob.glob(path + "*.png"):
    print(CleanUp)
    os.remove(CleanUp)

secs = (60-korrMin)*40 + intervall
korr = 0
minKorr = -1
in_file = ""
for sec in range(300,secs,intervall):
    m = int((sec + korr)/60)
    index = int(m/4)
    if(index <= 8):
        in_file = digs2(index) + ".png"
    ins = Image.open(in_file)
    width, height = ins.size
    inse = ins.resize((int(width/2), int(height/2)),1)
    insert = inse.convert("RGBA")


    s = sec - m*60 + korr
    if((s >= 60-intervall)):
        if(minKorr != m):
            minKorr = m
            korr += korrMin
        print(m)
        print(korr)
    img = Image.new('RGB', (1280,720), color = (18,18,18))
    name = digs2(m) + ":" + digs2(s)
    pasty = deepcopy(img)
    img.paste(insert, (100,150))

    i2 = m-index*4
    if(i2 == 3):
        imgblend = Image.blend(pasty,img,(60-intervall-s)/60)
    if(i2 == 2):
        imgblend = Image.blend(pasty,img,1)
    if(i2 == 1):
        imgblend = Image.blend(pasty,img,1)
    if(i2 == 0):
        imgblend = Image.blend(pasty,img,s/60)
    

    d = ImageDraw.Draw(imgblend)
    fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New Bold.ttf',16)
    d.text((100,100),name, font = fnt,fill=(255,255,255))


    imgblend.save(path + name + ".png")
