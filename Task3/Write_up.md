Sử dụng câu lệnh `$ ./bkcrack -L Keep_Out.zip` để xem bên trong file `Keep_Out.zip` thì thấy
~~~
Index Encryption Compression CRC32    Uncompressed  Packed size Name
----- ---------- ----------- -------- ------------ ------------ ----------------
    0 ZipCrypto  Deflate     64c4128b          686          327 bookmarks.txt
    1 ZipCrypto  Store       578dc79b       309359       309371 dat2fish stash.zip
    2 ZipCrypto  Deflate     22911de2          148          131 README.txt

~~~

File `bookmarks.txt` và `README.txt` được nén, còn file `dat2fish stash.zip` thì không được nén.

'50 4B 03 04 14 00 01 00 08 00 D7 9E 32 56' 

~~~
$ ./bkcrack -C Keep_Out.zip -c dat2fish\ stash.zip -p plaintext.txt 
~~~
~~~
bkcrack 1.5.0 - 2023-02-22
[12:32:10] Z reduction using 7 bytes of known plaintext
100.0 % (7 / 7)
[12:32:10] Attack on 960608 Z values at index 6
Keys: 4b2a3271 2b8bdad6 fa487e8e
65.6 % (629734 / 960608) 
[12:50:07] Keys
4b2a3271 2b8bdad6 fa487e8e
~~~
~~~
$ ./bkcrack -C Keep_Out.zip -k 4b2a3271 2b8bdad6 fa487e8e -U cracked_keep_out.zip 1234
~~~
~~~
$ ../bkcrack -L dat2fish\ stash.zip  
~~~
~~~
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
~~~
../bkcrack -C dat2fish\ stash.zip -c bookmarks.txt -P plain_bookmarks.zip -p plain_bookmarks.txt
~~~
~~~
bkcrack 1.5.0 - 2023-02-22
[13:05:21] Z reduction using 308 bytes of known plaintext
100.0 % (308 / 308)
[13:05:22] Attack on 27150 Z values at index 6
Keys: 99075ea6 102ed4f6 fcaa1b2b
71.6 % (19430 / 27150)
[13:06:01] Keys
99075ea6 102ed4f6 fcaa1b2b
~~~
~~~
../bkcrack -C dat2fish\ stash.zip -k 99075ea6 102ed4f6 fcaa1b2b -U cracked_dat2fish\ stash.zip 1234
~~~

    
 
