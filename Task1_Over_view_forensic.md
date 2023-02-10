#  Forensics tổng quan

Trong lĩnh vực an toàn thông tin, Forensics hay còn gọi là điều tra số là công việc phát hiện, bảo vệ và phân tích thông tin được lưu trữ, truyền tải hoặc được tạo ra bởi một máy tính hoặc mạng máy tính, nhằm đưa ra các suy luận hợp lý để tìm nguyên nhân, giải thích các hiện tượng trong quá trình điều tra.

Forensic được chia thành các mảng sau:

- File Forensics
- Network Forensics
- Memory Forensics
- Disk Forensics

## File Forensics (File Formats)

Một số khái niệm:

- File Signature là một giá trị dùng để xác định loại tệp. 
~~~txt
      Ví dụ:
      PNG -> 89 50 4E 47 0D 0A 1A 0A
      ZIP FILE -> 50 4B 03 04 or 50 4B 05 06
~~~


- Chunk là một đoạn (fragment) thông tin được sử dụng ở nhiều định dạng của tập tin đa phương tiện (multimedia file), chẳng hạn như PNG, MP3,... Mỗi chunk chứa một header cho biết một số tham số (ví dụ: loại chunk, comment, kích thước, v.v.). Theo sau header là một vùng chứa dữ liệu, được chương trình giải mã (decode) từ các tham số trong header.

- Checksum  là một chuỗi ngắn, duy nhất xuất phát từ việc chạy thuật toán mã hóa trên một file nhất định. Thuật toán xem xét tất cả các bit tạo nên một file và dựa trên những bit duy nhất đó, tạo ra một checksum. Nó được sử dụng để kiểm tra tính toàn vẹn dữ liệu để đảm bảo tập tin không bị hỏng trong quá trình tải xuống (download) và tệp không bị nhiễm phần mềm độc hại (malware) hoặc phần mềm độc hại khác.

- Lossless Compression (Nén không mất dữ liệu) là làm giảm kích thước file mà không làm giảm chất lượng.

- Lossy Compression (Nén mất dữ liệu): là làm giảm kích thước file mà chất lượng và dữ liệu bị mất so với phiên bản gốc.

Công cụ thường dùng:

- Binwalk: Trích xuất file nằm trong một file khác.

- HxD: trình xoạn thảo mã hex trong file

## Network Forensics

Là một nhánh của điều tra số liên quan đến việc theo dõi, giám sát, phân tích lưu lượng mạng máy tính nhằm phục vụ cho việc thu thập thông tin, sự kiện liên quan,để phát hiện sự bất thường, các dấu hiệu xâm nhập trên môi trường mạng.

Các công cụ phổ biến :

- Wireshark, Network Miner bắt và phân tích gói tin với giao diện đồ họa
- Tcpdump, tshark phân tích gói tin với giao diện console
- p0f dùng để phát hiện hệ điều hành, console trên nền Linux
- netcat, debug kết nối, đóng vai trò cả client và server, console trên windows và linux
- Snort, opensource phát hiện xâm nhập
- Nmap, tcpxtract, ssldump, nslookup, maxmind... và rất nhiều công cụ khác

## Memory Forensics

Là phương thức điều tra máy tính bằng việc sử dụng kiến trúc quản lý bộ nhớ trong máy tính để ánh xạ, trích xuất các tập tin đang thực thi và cư trú trong bộ nhớ RAM tại thời điểm hệ thống đang hoạt động, sau đó tiến hành phân tích làm rõ các hành vi đang xảy ra trên hệ thống.

Những đặc điểm nổi bật của mảng này là:

- Dữ liệu cần phân tích thường lớn hoặc rất lớn.
- Dữ liệu có thể không còn nguyên vẹn, bị thay đổi, bị phần mảng.
- Dữ liệu dễ dàng bị giả mạo

Khi làm công việc Memory Forensics, có một số các công cụ hỗ trợ dưới đây:

- DumpIt, FTK Imager: dump dữ liệu từ RAM trên Windows.
- Volatility là một framework với rất nhiều plugins được dùng để phân tích và tìm kiếm thông tin từ chứng cứ thu được. Các plugins được viết để phân tích điều tra bộ nhớ theo kiến trúc của hệ điều hành windows. Một số plugin phổ biến:
~~~txt
   - imageinfo: xác định hệ điều hành, gói dịch vụ và kiến trúc phần cứng(32 hoặc 64 bit).
   - pslist: lấy thông tin các tiến trình. Tuy nhiên nó không liệt kê được các tiến trình ẩn hoặc bị kết thúc.
   - pstree: hiện thị danh sách tiến trình dưới dạng cây. Từ đó dễ xác định được tiến trình cha, con. Nhược điểm cũng giống như câu lệnh pslist.
   - psscan: lấy thông tin các tiến trình. Khắc phục được nhược điểm của hai câu lệnh trên.

~~~


## Disk Forensics

Là việc thu thập, phân tích dữ liệu được lưu trữ trên phương tiện lưu trữ vật lý, từ đó trích xuất các dữ liệu ẩn, khôi phục các tập tin bị xóa, qua đó xác định người đã tạo ra những thay đổi dữ liệu trên thiết bị được phân tích, cũng như tìm kiếm những bằng chứng liên quan đến hoạt động xâm nhập, gian lận…


Công cụ thường dùng: ADS Locator, Disk Investigator, Passware Encryption Analyzer, Disk Detector, Sleuth Kit, FTK,... 

# Steganography

1. Khái niệm

Là nghệ thuật và khoa học về việc giấu thông điệp, hình ảnh, hoặc dữ liệu trong một thông điệp khác, hỉnh ảnh khác hoặc dữ liệu khác. Thông thường, thông điệp ẩn sẽ được ẩn dấu trong một ảnh, một bài viết, một đoạn văn bản, hay thậm chí là một danh sách mua sắm. Ví dụ cụ thể: thông điệp ẩn có thể được viết bằng mực vô hình (invisible ink), nằm giữa các dòng chữ nhìn thấy được bởi mắt thường của một bức thư.

2. Phân biệt Steganography và Cryptography

Ưu điểm của Steganography so với Cryptography là thông điệp bí mật không gây bất kì sự chú ý nào từ phía đối tượng giám sát bởi nó đã được giấu đi. Tất nhiên điều này tốt hơn so với một thông điệp đã được mã hóa nhưng lại không ẩn đi ( ở đây không nói đến việc thông điệp này có thể giải mã được không ) mà để cho người ta nhìn thấy và quan tâm.
Kết hợp Steganography với Cryptography một cách hợp lý, ta sẽ đảm bảo được tính an toàn của thông điệp hơn nhiều lần.

3. Phương pháp LSB (LEAST SIGNIFICANT BIT) 
 
 Trong xử lý ảnh, mỗi pixel nói chung được lưu dưới dạng 8 bit hay 24 bit. Với biểu diễn 24 bit, mỗi pixel trải trên 3 byte, mỗi byte ứng với các màu đỏ, xanh da trời và xanh lá cây (RGB). Các màu là sự kết hợp của 3 màu trên. Mỗi byte có giá trị từ 0 - 255 ứng với cường độ màu. Màu tối nhất có giá trị 0, màu sáng nhất có giá trị 255.
 
 Có rất nhiều phương pháp để che giấu thông tin trong các hình ảnh số nhưng phương pháp dụng nhất là chèn bit có trọng số nhỏ nhất (LSB). Ví dụ ta có: 11110110 là một số nhị phân 8 bit. Bit tận cùng bên phải ( bit 0 ) được gọi là bit LSB vì sự thay đổi của nó có ảnh hưởng ít nhất đến giá trị của số. Dữ liệu nhị phân của thông báo mật sẽ bị chia nhỏ ra và thay thế các bit LSB của từng byte trong giá trị RGB của từng Pixel. Sỡ dĩ chúng ta chỉ thay thế các bit LSB là vì sau khi thay đổi các giá trị trong RBG chỉ dao động 1 đơn vị, dùng mắt thường sẽ khó phát hiện ra sự thay đổi của bức ảnh, giúp đạt được mục đích ẩn dấu.
Bởi mỗi pixel được tạo nên từ 3 kênh màu (RGB), nên ta có thể dấu tối đa 3 bit của thông báo mật.

 Tóm gọn lại thì ta có các bước để dấu một thông điệp ẩn vào một bức ảnh bằng phương pháp LSB:
 
- Chuyển thông điệp bí ẩn sang dạng nhị phân.
- Thay từng 3 bit của thông điệp vào LSB của các pixel liên tiếp trong ảnh cho đến khi hết thông điệp.
- Lưu lại bức ảnh mới đã chứa thông điệp mật của ta.

 Việc thực hiện dấu thông tin bằng LSB này hoàn toàn thực hiện được bằng một đoạn code ngắn mà bạn tự viết ra. Nếu không bạn có thể sử dụng các phần mềm có sẵn trên mạng để thực hiện thay. Ví dụ như: Jsteg(cho file JEPG), Zsteg(cho file BMP, PNG). 

4. Một số tool phổ biến

 Dùng để sàng, lọc thông tin trong file:

 - Exiftool
 - GHex
 - Binwalk
 - Steghide
 - Stegdetect
 - Stegcracker
 - Zbarimg
 - GPG

  Phân tích file ảnh:
 
 - Stegsolve
 - Stegoveritas
 
  Phân tích file PDF:
 
 - Peepdf
 
  Phân tích file âm thanh:
 
 - Audacity
 - Sonic Visualiser
 - Deep Sound
 
