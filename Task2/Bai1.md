Mở file ra thì em thấy phần Sisnature, IHDR, IDAT bị sai.
![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-16%20222516.png)

Và sửa như sau:

- Signature: `CF 50 22 26 0D 6D 61 72` -> `89 20 4E 47 0D 0A 1A 0A`
- IHDR: `49 78 44 20` -> `49 48 44 52`
- IDAT: `49 44 41 0B` -> `49 44 41 54`

![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-16%20222906.png)

Em check IEND chunk và thấy nó cũng bị sai

![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-16%20222530.png)

Sửa: `49 45 7A 2A` -> `49 45 4E 44`

![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-16%20222545.png)


Mở file lên, thấy ảnh đã xem được

![](https://github.com/HuyThang25/Training_Forensics/blob/main/Task2/Bai1.png)
