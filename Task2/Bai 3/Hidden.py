from PIL import Image
def convert_text_to_bin(str):
    '''Chuyển từ văn bản sang nhị phân'''
    binary_key = [bin(ord(c))[2:].rjust(8,'0') for c in str]  # remove '0b' from string, fill 8 bits
    binary_key = ''.join(binary_key)
    return binary_key
def hid_bit(bit,vt,value):
    '''Giấu bit vào màu
        bit: bit cần giấu
        vt: vị trí bit trong màu
        value: giá trị màu
    '''
    tail = (int(bit)<<vt)+(value&vt)
    return (value>>(vt+1)<<(vt+1)) + tail


img = Image.open('D:\GitHub\Training_Forensics\Task2\Bai1.png')
pixels = img.load()

key = convert_text_to_bin('Bui Huy Thang')
key = key + (3-(len(key)%3))*'00000000'

new_img = Image.new(img.mode, img.size)
pixels_new = new_img.load()
width = img.size[0]
height = img.size[1]

for i in range(width):
  for j in range(height):
    pixels_new[i,j] = pixels[i,j]   
    
for i in range(len(key)//3):
  r,g,b = pixels[i%width,i//width]
  pixels_new[i%width,i//width]  = (hid_bit(key[i*3],1,r),hid_bit(key[i*3+1],0,g),hid_bit(key[i*3+2],2,b))


new_img.save('New_Image.png')



