from PIL import Image

def get_hidden_bit(value,vt):
    return (value>>vt)&1
img = Image.open('New_Image.png')
pixels = img.load()

key=[]
width = img.size[0]
height = img.size[1]
for i in range(width):
  for j in range(height):
    r,g,b = pixels[j,i]
    key.append(str(get_hidden_bit(r,1)))
    key.append(str(get_hidden_bit(g,0)))
    key.append(str(get_hidden_bit(b,2)))

key = ''.join(key)
key = [chr(int(key[i:i+8], 2)) for i in range(0,len(key),8)]
key = ''.join(key)

f = open('output.txt','w',encoding='utf-8')
key.encode('utf-8')
f.write(key)
f.close()

