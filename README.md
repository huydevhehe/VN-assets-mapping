# 🌊 VN Assets Mapping - Hydraulic GIS Dashboard

A professional, interactive GIS Dashboard for monitoring hydraulic infrastructure across Vietnam (Reservoirs, Sluices, Pumping Stations). This system handles large-scale geospatial data and performs real-time coordinate transformations from VN-2000 to WGS84.

## 🚀 Key Features
- **VN-2000 to WGS84 Transformation**: Automatically converts industry-standard Vietnamese coordinates to international map standards with high precision.
- **Smart Marker Clustering**: Effortlessly handles 1,000+ data points without performance lag using advanced clustering techniques.
- **Dynamic Infrastructure Filtering**: Filter assets by River Basins or Provinces/Cities.
- **High-End UI**: Premium "Light Mode" design with Glassmorphism effects and customized iconography (🌊 Reservoirs, 🚪 Sluices, ⚡ Pumping Stations).
- **Dual Coordinate Display**: Side-by-side comparison of raw VN-2000 data and mapping coordinates for technical validation.

## 🛠️ Tech Stack
- **Leaflet.js**: Core Interactive Map engine.
- **Proj4js**: Coordinate system transformation logic.
- **MarkerCluster**: Performance optimization for big data.
- **GeoJSON**: Lightweight geospatial data interchange.
- **CartoDB Positron**: Modern, clean map tile layer.

---

# 🌊 Hệ thống Giám sát Hạ tầng Thủy lợi Việt Nam

Hệ thống Dashboard GIS chuyên nghiệp dùng để giám sát các công trình thủy lợi trên toàn lãnh thổ Việt Nam (Hồ chứa, Cống, Trạm bơm). Hệ thống có khả năng xử lý dữ liệu lớn và chuyển đổi tọa độ VN-2000 sang WGS84 theo thời gian thực.

## 🚀 Tính năng nổi bật
- **Chuyển đổi tọa độ VN-2000**: Tự động chuyển đổi từ tọa độ chuyên ngành Việt Nam sang chuẩn bản đồ quốc tế với độ chính xác cao.
- **Gom nhóm thông minh (Clustering)**: Xử lý mượt mà hơn 1.000 điểm dữ liệu mà không gây lag trình duyệt.
- **Bộ lọc linh hoạt**: Lọc công trình theo Lưu vực sông hoặc theo Tỉnh/Thành phố.
- **Giao diện cao cấp**: Thiết kế Light Mode hiện đại, sử dụng hiệu ứng kính mờ (Glassmorphism) và bộ biểu tượng đặc thù.
- **Hiển thị tọa độ kép**: Cho phép đối chiếu trực tiếp dữ liệu sổ sách (VN-2000) và vị trí trên bản đồ (WGS84).

## 🖥️ Cách chạy dự án (How to run)
1. **Clone project**:
   ```bash
   git clone https://github.com/huydevhehe/VN-assets-mapping.git
   ```
2. **Chạy Local Server**: 
   Dự án sử dụng các tệp JSON cục bộ, bạn cần chạy qua một server ảo để tránh lỗi bảo mật trình duyệt (CORS).
   - Nếu dùng **VS Code**: Chuột phải vào `index.html` chọn **Open with Live Server**.
   - Nếu máy có **Python**: Chạy lệnh `python -m http.server 8000`.
   - Sau đó truy cập: `http://localhost:8000`

---
*Developed by **Nguyen Quoc Huy***
