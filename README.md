# 🌊 Vietnam GIS Hydraulic & River Network Dashboard

An advanced, high-performance GIS Dashboard for monitoring and visualizing large-scale hydraulic infrastructure and river networks across Vietnam. Optimized to handle over **250,000 geospatial features** with real-time interactivity.

---

## 🇺🇸 English Version

### 🚀 Key Features
- **Extreme Scale Geospatial Data**: Manages 250,000+ river segments (LineStrings) and 5,000+ water bodies (Polygons) with zero lag.
- **High-Performance Canvas Rendering**: Utilizes the HTML5 Canvas API for ultra-fast vector drawing, ensuring 60FPS performance even with massive datasets.
- **Adaptive Zoom Rendering**: Dynamic level-of-detail (LOD) system that toggles complex river networks based on zoom levels to optimize browser RAM.
- **Regional Data Strategy**: Data is split into North, Central, and South regions to facilitate faster initial loading and efficient memory management.
- **Coordinate Transformation**: Seamlessly converts industry-standard **VN-2000** coordinates to international **WGS84** standards.

### 🛠️ Tech Stack
- **Leaflet.js**: Core Interactive Map engine.
- **HTML5 Canvas**: Optimized rendering layer for big data.
- **Git LFS**: Storage management for large geospatial JSON files (>400MB).
- **Proj4js**: High-precision coordinate system transformations.

### 📦 Installation & Setup
1. **Clone & Initialize LFS**:
   ```bash
   git clone https://github.com/huydevhehe/VN-assets-mapping.git
   cd VN-assets-mapping
   git lfs install
   git lfs pull
   ```
2. **Run Locally**:
   Use a local server to avoid CORS issues:
   - **VS Code**: Use "Live Server" extension.
   - **Python**: `python -m http.server 8000`

---

## 🇻🇳 Tiếng Việt

### 🚀 Tính năng nổi bật
- **Xử lý dữ liệu GIS quy mô lớn**: Hiển thị mượt mà hơn 250.000 đoạn sông/kênh và 5.000 hồ chứa trên toàn quốc.
- **Công nghệ Canvas Renderer**: Sử dụng API Canvas để vẽ hàng trăm nghìn đối tượng vector, đảm bảo trải nghiệm mượt mà 60FPS.
- **Hiển thị thông minh theo Zoom**: Tự động lọc và chỉ hiển thị chi tiết mạng lưới sông ngòi khi người dùng phóng to (Zoom Level >= 10), giúp tối ưu bộ nhớ.
- **Phân vùng dữ liệu Miền**: Chia dữ liệu thành 3 tệp riêng biệt (Bắc - Trung - Nam) để tối ưu hóa tốc độ tải và khả năng xử lý của trình duyệt.
- **Chuyển đổi VN-2000**: Tự động chuyển đổi từ hệ tọa độ chuyên ngành Việt Nam sang chuẩn bản đồ quốc tế.

### 🛠️ Công nghệ sử dụng
- **Leaflet.js**: Thư viện bản đồ tương tác chính.
- **Canvas API**: Render dữ liệu lớn không gây lag.
- **Git LFS**: Quản lý các file dữ liệu JSON nặng (>400MB) trên GitHub.
- **Python Data Engine**: Bộ script cào và tiền xử lý dữ liệu GIS.

### 🖥️ Cách khởi chạy
1. **Tải mã nguồn và dữ liệu**:
   ```bash
   git clone https://github.com/huydevhehe/VN-assets-mapping.git
   cd VN-assets-mapping
   git lfs install
   git lfs pull
   ```
2. **Chạy Local Server**: 
   - Sử dụng **Live Server** trên VS Code hoặc chạy lệnh: `python -m http.server 8000`.

---
*Developed by **Nguyen Quoc Huy***
