# 🌊 VN Assets Mapping - Hệ thống Đối soát Hạ tầng Thủy lợi Việt Nam

Hệ thống bản đồ số tích hợp dữ liệu mạng lưới sông ngòi, kênh mương và vùng nước toàn quốc được trích xuất và đối soát trực tiếp từ cơ sở dữ liệu Quy hoạch Thủy lợi Việt Nam.

![Screenshot](https://img.shields.io/badge/Data-100%25_Accurate-brightgreen)
![Features](https://img.shields.io/badge/Features-8_Clusters_|_Lazy_Loading-blue)

## 🚀 Tính năng nổi bật (Bản Pro 8 Cụm)
- **Độ chính xác tuyệt đối**: Cào và đối soát thành công **250.333 đoạn sông (Line)** và **5.697 vùng nước (Polygon)** từ server gốc của Bộ.
- **Giải pháp "Chia để trị"**: Dữ liệu được chia thành 8 cụm (Cluster) từ Bắc vào Nam giúp tối ưu hóa RAM và tốc độ tải.
- **Lazy Loading (Tải theo yêu cầu)**: Chỉ tải dữ liệu khi người dùng chọn vùng cụ thể, đảm bảo trình duyệt luôn mượt mà.
- **Tách lớp thông minh**: Cho phép bật/tắt riêng biệt lớp **Sông chi tiết** và **Vùng nước lớn** để tránh chồng chéo.
- **Full Thuộc tính (100% Attributes)**: Hiển thị đầy đủ thông tin gốc (Tên sông, độ rộng, chiều dài, diện tích, ngày cập nhật...).
- **Giao diện Modern**: Thiết kế Sidebar theo phong cách tối giản, hiện đại và dễ sử dụng.

## 📊 Thống kê dữ liệu
| Cụm vùng | Phạm vi tỉnh thành | Trạng thái |
| :--- | :--- | :--- |
| **Cụm 1** | Hà Giang, Cao Bằng, Lào Cai, Bắc Kạn, Lạng Sơn... | ✅ Sẵn sàng |
| **Cụm 2** | Vĩnh Phúc, Bắc Ninh, Quảng Ninh, Hải Phòng, Hà Nội... | ✅ Sẵn sàng |
| **Cụm 3** | Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Bình, Quảng Trị | ✅ Sẵn sàng |
| **Cụm 4** | Thừa Thiên Huế, Đà Nẵng, Quảng Nam, Quảng Ngãi... | ✅ Sẵn sàng |
| **Cụm 5** | Kon Tum, Gia Lai, Đắk Lắk, Đắk Nông, Lâm Đồng | ✅ Sẵn sàng |
| **Cụm 6** | Đông Nam Bộ (TP.HCM, Đồng Nai, Bình Dương...) | ✅ Sẵn sàng |
| **Cụm 7** | Miền Tây Nhóm 1 (Long An, Tiền Giang, An Giang...) | ✅ Sẵn sàng |
| **Cụm 8** | Miền Tây Nhóm 2 (Cần Thơ, Sóc Trăng, Cà Mau...) | ✅ Sẵn sàng |

## 🛠️ Công nghệ sử dụng
- **Leaflet.js**: Nền tảng bản đồ tương tác.
- **CartoDB Positron**: Bản đồ nền tối giản, làm nổi bật dữ liệu chuyên ngành.
- **Git LFS**: Quản lý tệp dữ liệu JSON dung lượng lớn (>500MB).
- **Python GIS Engine**: Bộ công cụ tự động hóa việc thu thập và phân vùng tọa độ.

## 🖥️ Hướng dẫn khởi chạy
1. **Clone project**:
   ```bash
   git clone https://github.com/huydevhehe/VN-assets-mapping.git
   cd VN-assets-mapping
   git lfs install
   git lfs pull
   cd VN-assets-mapping
   git lfs install
   git lfs pull
   ```
2. **Chạy Local Server**: 
   - Sử dụng **Live Server** trên VS Code hoặc:
   ```bash
   python -m http.server 8000
   ```
3. **Truy cập**: `http://localhost:8000`

---
*Phát triển bởi **Nguyen Quoc Huy***
