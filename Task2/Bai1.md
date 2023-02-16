Mở file ra thì em thấy phần Sisnature, IHDR, IDAT bị sai.

Và sửa như sau:

Signature: `CF 50 22 26 0D 6D 61 72` -> `89 20 4E 47 0D 0A 1A 0A`
IHDR: `49 78 44 20` -> `49 48 44 52`
IDAT: `49 44 41 0B` -> `49 44 41 54`


Em check IEND chunk và thấy nó cung bị sai


Và sửa: `49 45 7A 2A` -> `49 45 4E 44`
![](https://drive.google.com/file/d/1CFr7NorRtLx7uh_ijdVSqirb9jUOeuS2/view?usp=share_link)
![](https://drive.google.com/file/d/1CFr7NorRtLx7uh_ijdVSqirb9jUOeuS2/view?usp=share_link)
![]()
![]()
