~~~py
import struct
import zlib

def readChunk(f):
  '''Lấy dữ liệu 1 chunk trong file'''
  
  chunkLength, chunkType = struct.unpack('>I 4s',f.read(8))
  chunkData = f.read(chunkLength)
  chunk_crc = struct.unpack('>I',f.read(4))
  return chunkType,chunkData

def showHex(bytes):
  str = bytes.hex()
  for i in range(len(str)//2):
    print(f'{str[i*2]}{str[i*2+1]} ',end='')
  print('')
  
# ---------------------------------------------------------------
f = open('Bai1.png', 'rb')

# Lấy PNG Signature (8 bytes)
PngSignature = f.read(8)
showHex(PngSignature)
#Lấy Chunk IDHR
IDHR = readChunk(f)
width, height, bitDepth, colorType, compression, filter, interlace = struct.unpack('>IIBBBBB',IDHR[1])
# print('Width:',width)
# print('Height:',height)
# print('Bit depth:',bitDepth)
# print('Color Type:',colorType)
# print('Compresssion method:',compression)
# print('Filter method:',filter)
# print('Interlace method:',interlace)

#Lấy và giải nén các chunk IDAT
IDAT_data=[]
while (True):
  chunk=readChunk(f)
  if chunk[0]==b'IEND': break
  IDAT_data.append(chunk[1])

totalData = b''.join(IDAT_data)
totalData = zlib.decompress(totalData)

def PaethPredictor(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        Pr = a
    elif pb <= pc:
        Pr = b
    else:
        Pr = c
    return Pr

#Phân tích các pixel
Recon = []
bytesPerPixel = 3
stride = width * bytesPerPixel

def Recon_a(r, c):
    return Recon[r * stride + c - bytesPerPixel] if c >= bytesPerPixel else 0

def Recon_b(r, c):
    return Recon[(r-1) * stride + c] if r > 0 else 0

def Recon_c(r, c):
    return Recon[(r-1) * stride + c - bytesPerPixel] if r > 0 and c >= bytesPerPixel else 0

i = 0
for r in range(height): # for each scanline
    filter_type = totalData[i] # first byte of scanline is filter type
    i += 1
    for c in range(stride): # for each byte in scanline
        Filt_x = totalData[i]
        i += 1
        if filter_type == 0: # None
            Recon_x = Filt_x
        elif filter_type == 1: # Sub
            Recon_x = Filt_x + Recon_a(r, c)
        elif filter_type == 2: # Up
            Recon_x = Filt_x + Recon_b(r, c)
        elif filter_type == 3: # Average
            Recon_x = Filt_x + (Recon_a(r, c) + Recon_b(r, c)) // 2
        elif filter_type == 4: # Paeth
            Recon_x = Filt_x + PaethPredictor(Recon_a(r, c), Recon_b(r, c), Recon_c(r, c))
        else:
            raise Exception('unknown filter type: ' + str(filter_type))
        Recon.append(Recon_x & 0xff) # truncation to byte

f.close()

f = open('RGB.txt','w')

for i in range(len(Recon)//3):
  f.write(f'({Recon[i*3]},{Recon[i*3+1]},{Recon[3*i+2]})')
f.close()
~~~