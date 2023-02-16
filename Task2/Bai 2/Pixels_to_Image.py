import re
from PIL import Image

f = open("Task2\RGB.txt", "r", encoding="utf-8")
pixels = []
scanline = f.readline()

while scanline !='':
    scanline = re.findall(r'\d+',scanline)
    pixels.append([tuple(scanline[i:i+3]) for i in range(0,len(scanline),3)])
    scanline = f.readline()
    
width = len(pixels[0])
height = len(pixels)
new_img = Image.new("RGB", (width,height))
pixels_new = new_img.load()

for i in range(width):
    for j in range(height):
        pixels_new[i,j] = tuple(int(value) for value in pixels[j][i])
new_img.show()


