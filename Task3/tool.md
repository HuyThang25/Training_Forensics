# Tool John The Ripper

John The Ripper (JtR) là một công cụ được sử dụng để crack hash. Đây là một công cụ trên giao diện dòng lệnh và cũng có thể cài trên nhiều hệ điều hành khác nhau như MacOS, Windows và Linux. JtR được thiết kế rất dễ sử dụng và có tích hợp cả tính năng tự động nhận diện thuật toán hash, thế nên chúng ta không cần phải xác định thuật toán rồi mới crack giống như Hashcat.

Cú pháp của John The Ripper rất đơn giản như sau:
~~~
$ john <file-chứa-hash>
~~~

Để lấy mã băm từ file ta có thể sử dụng hai tool: zip2john (đối với file Zip), rar2john (đối với file Rar).

Khi sử dụng câu lệnh john như trên, John The Ripper sẽ chạy để tìm thuật toán hash, sau đó sẽ sử dụng danh sách mặc định của mính để crack hash. Quá trình này sẽ tốn rât nhiều thời gian so với khi bạn cung cấp cho John trên của thuật toán hash, nhưng trong trường hợp chúng ta không thể tìm được tên thuật toán hash thì đành phải chấp nhận.

Cung cấp thuật toán hash sử dụng câu lệnh sau

~~~
$ john --format=<tên-thuật-toán> <file-chứa-hash>
~~~

Để xem  danh sách thuật toán, sử dụng câu lệnh :

~~~
$ john --list=formats
~~~

![](https://github.com/HuyThang25/Image/blob/main/Screenshot%202023-02-24%20190708.png)

Các phương pháp bẻ khoá mật khẩu

## Sử dụng tấn công từ điển

Tấn công từ điển là hình thức tấn công bằng cách thử qua nhiều mật khẩu tiềm năng để tìm ra mật khẩu đúng. Danh sách các mật khẩu tiểm năng được lấy trong từ điển và có thể liên quan đến tên người dùng, sinh nhât, sở thích... hay đơn giản giản là các từ phổ biến như "password"... Một chương trình máy tính có thể chạy hàng triều từ trong vài giờ.

John được trang bị một danh sách password riêng, mặc dù danh sách này khá hạn chế và không thể so sánh với rockyou.txt. Danh sách mặc định của John The Ripper có path như sau: `/usr/share/john/password.lst`

John sẽ nhân vào 1 wordlist ta cho trước, sau đó tạo hash của từng từ bến trong worlist đó, rồi so sánh với hash cần crack. Nếu giống nhau thì crack thành công.

Để thực hiện tấn công từ điển ta thêm `--wordlist=<Path>' vào câu lệnh. Trong đó `Path` là đường dẫn tới wordlist.

## Tấn công brute-force 

Brute force là một trong những hình thức phổ biến nhất của tấn công mật khẩu và dễ dàng nhất để thực hiện. Brute force thường là biện pháp cuối cùng của hacker nếu các kỹ thuật trước đó thất bại, đơn giản vì đây là công cụ tốn nhiều thời gian nhất.

John ghép thử tất cả các ký tự thành một password có độ dài cho trước, sau đó tạo hash của password đó rồi so sánh với hash cần crack. Nếu giống nhau thì crack thành công. 

Để thực hiện tấn công brute-force ta thêm `-i:<độ-dài-pass>` vào câu lệnh. Trong đó -i để vào Incremental mode. 

# Tool Hashcat

# Tool pkcrack

# Tool bkcrack

# Điểm khác biệt giữa pkcrack và bkcrack
