# Cấu trúc file PNG

## File Signature

8 bytes đầu tiên của một file PNG luôn chứa giá trị sau: `89 50 4E 47 0D 0A 1A 0A` (dạng Hex)

Trong đó:

- Hai byte đấu tiên `80 50`: phân biệt PNG với các định dạng khác trên hệ thống
- Byte thứ 3 đến 5 `50 4E 47`: nêu tên định dạng file (PNG)
- Hai byte tiếp theo `0D 0A`: là 2 byte `CR(\n)-LF(\n)`, nhận diện lỗi truyền kém làm thay đổi trình tự dòng
- Byte kế tiếp `1A`: là kí tự `Ctrl-Z` để ngưng hiển thị tệp trong MS-DOS
- Byte cuối `0A`: là kí tự `LF(\n)`, kiểm tra quá trình dịch CR-LF có bị đảo ngược hay không.

## Các Chunks

Mỗi chunk cấu tạo từ 4 phần: 

 - Length: là một số nguyên 4 byte không dấu cho biết độ dài phần dữ liệu của chunk
 - Chunk Type: là một đoạc code 4 byte, cho biết tên của loại chunk đó
 - Chunk data: các byte dữ liệu của loại chunk tương ứng
 - CRC: có độ dài 4 byte, được tính dựa trên chunk type và chunk data nhằm kiểm tra tính toàn ven của chunk data

 

### IDHR (IMAGE HEADER) :

- Phải xuất hiện đầu tiên. 
- Trường dữ liệu của chunk IDHR bao gồm: 

  - Width (Độ Rộng): 4 bytes, cho biết số pixel của chiều ngang ảnh

  - Height (Độ Cao): 4 bytes, cho biết số pixel của chiều dọc ảnh

  - Bit depth (Độ sâu màu): 1 byte

  - Color type (Dạng màu): 1 byte

  - Compression method (Phương pháp nén): 1 byte

  - Filter method (Phương pháp lọc): 1 byte

  - Interlace method (Phương pháp đan xen): 1 byte

### IEND (IMAGE TRAILER):  
-  Phải xuất hiện cuối cùng.
-  Nó đánh dấu sự kết thúc của dòng dữ liệu PNG. 
-  Trường dữ liệu trong chunk này sẽ được bỏ trống.

### IDAT (IMAGE DATA): 
- Chứa dữ liệu màu của hình ảnh. 
- Một bức ảnh có một hoặc nhiều IDAT. Nếu có nhiều thì chúng phải nằm liên tiếp nhau.

### PLTE (PALETTE):  

- Phải xuất hiện khi color type có giá trị bằng 3, có thể xuất hiện hoặc không ở color type 2 và 6, và không được xuất hiện ở color type 0 và 4.
- Nếu chunk này xuất hiện thì nó sẽ nằm trước IDAT chunk đầu tiên. Không được có nhiều hơn một 


Ngoải ra còn có một số chunk không bắt buộc như: 
![](https://user-images.githubusercontent.com/93728466/219398088-5acc7770-9dd7-413c-8c6d-e36aca5ed475.png)
