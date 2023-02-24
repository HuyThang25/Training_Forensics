# Crack file `Keep_Out.zip`

Sử dụng tool John The Ripper, tấn công từ điển:

![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-24%20232919.png)

Tìm được pass là `MANCHESTERUNITED`. Giải nén file ta được các file sau:

![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-24%20225518.png)

# Crack file `dat2fish stash.zip` 

## Cách 1: crack bằng file `bookmarks.txt` 

Mở file `dat2fish stash.zip` ra
~~~
$ ../bkcrack -L dat2fish\ stash.zip  
bkcrack 1.5.0 - 2023-02-22
Archive: dat2fish stash.zip
Index Encryption Compression CRC32    Uncompressed  Packed size Name
----- ---------- ----------- -------- ------------ ------------ ----------------
    0 ZipCrypto  Deflate     64c4128b          686          327 bookmarks.txt
    1 ZipCrypto  Deflate     b2e230df        74956        69375 confidential.pdf
    2 ZipCrypto  Deflate     eff137ca       143497       141734 favmusic.mp3
    3 ZipCrypto  Deflate     e0ec1780        48292        47846 meme.jpg
    4 ZipCrypto  Deflate     fe719fc9        50996        49367 uno-reverse.png
~~~
Thấy file `bookmarks.txt`  có cùng kích cỡ với file bookmarks vừa tìm được => file trước là bản rõ.

Vì file `bookmarks.txt` bị nén nên trước khi crack sử dụng công cụ 7z để nén lại lưu thành `plain_bookmarks.zip` 

Sử dụng câu lệnh sau để tìm key:
~~~
../bkcrack -C dat2fish\ stash.zip -c bookmarks.txt -P plain_bookmarks.zip -p plain_bookmarks.txt
bkcrack 1.5.0 - 2023-02-22
[13:05:21] Z reduction using 308 bytes of known plaintext
100.0 % (308 / 308)
[13:05:22] Attack on 27150 Z values at index 6
Keys: 99075ea6 102ed4f6 fcaa1b2b
71.6 % (19430 / 27150)
[13:06:01] Keys
99075ea6 102ed4f6 fcaa1b2b
~~~
Sau khi có key thì khôi phục lại file:
~~~
../bkcrack -C dat2fish\ stash.zip -k 99075ea6 102ed4f6 fcaa1b2b -U cracked_dat2fish\ stash.zip 1234
~~~
Giải nén và mở file `confidential.pdf`, bôi đen phần màu đen ta sẽ được flag: `HCMUS-CTF{H0w_D1d_y0U_Kn0W_Th3_P@ssW0rd????}`

## Cách 2: không sử dụng file `bookmarks.txt`

Sau một hồi tìm hiểu các cấu trúc file pdf, jpg, png thì em thấy file png là file có thể đoán dễ nhất => Sử dụng file `uno_reverse.png` để crack.

Sử dụng HxD để lưu các byte sau `89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52` (Signature + 8-bytes đầu của IHDR chunk) vào file plaintext.txt

Rồi sử dụng tool bkcrack để dò key mà không tìm được. Em cũng thử nén file plaintext.txt lại rồi dò cũng không ra.
