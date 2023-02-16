from PIL import Image

img = Image.open('D:\GitHub\Training_Forensics\Task2\Bai1.png')
pixels = img.load()
f = open('D:\GitHub\Training_Forensics\Task2\RGB.txt','w')

for i in range(img.size[0]):
    for j in range(img.size[1]):
        f.write(str(pixels[i,j]))
    f.write('\n')
f.close()