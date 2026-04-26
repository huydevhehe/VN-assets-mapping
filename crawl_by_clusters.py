import requests
import json
import time
import os

# Dinh nghia 8 vung tu Bac vao Nam dua tren Vi do (Latitude)
VUNG_CONFIG = [
    {"id": 1, "name": "Cụm 1 - Cực Bắc (Hà Giang, Cao Bằng, Lào Cai...)", "lat_min": 22.2},
    {"id": 2, "name": "Cụm 2 - Đông Bắc & Tây Bắc (Sơn La, Yên Bái, Tuyên Quang...)", "lat_min": 21.2},
    {"id": 3, "name": "Cụm 3 - Đồng bằng Sông Hồng (Hà Nội, Hải Phòng, Quảng Ninh...)", "lat_min": 20.2},
    {"id": 4, "name": "Cụm 4 - Bắc Trung Bộ (Thanh Hóa, Nghệ An, Hà Tĩnh...)", "lat_min": 18.2},
    {"id": 5, "name": "Cụm 5 - Trung Trung Bộ (Quảng Bình, Huế, Đà Nẵng, Quảng Nam...)", "lat_min": 15.5},
    {"id": 6, "name": "Cụm 6 - Nam Trung Bộ & Tây Nguyên (Bình Định, Đắk Lắk, Gia Lai...)", "lat_min": 12.5},
    {"id": 7, "name": "Cụm 7 - Đông Nam Bộ (TP.HCM, Bình Dương, Đồng Nai, Bà Rịa...)", "lat_min": 10.5},
    {"id": 8, "name": "Cụm 8 - Tây Nam Bộ (Long An, Tiền Giang, Cần Thơ, Cà Mau...)", "lat_min": 0.0}
]

def get_vung_info(geometry):
    try:
        if not geometry: return VUNG_CONFIG[0]
        coords = geometry['coordinates']
        while isinstance(coords, list) and len(coords) > 0 and isinstance(coords[0], list):
            coords = coords[0]
        
        if isinstance(coords, list) and len(coords) >= 2:
            lat = coords[1]
            for v in VUNG_CONFIG:
                if lat >= v["lat_min"]:
                    return v
        return VUNG_CONFIG[-1]
    except:
        return VUNG_CONFIG[0]

def crawl_by_clusters(layer_name, total_features, prefix):
    base_url = "http://bando.quyhoachthuyloi.vn/geoserver/wfs"
    page_size = 1500
    
    # Khoi tao ket qua cho 8 vung
    cluster_results = {v["id"]: [] for v in VUNG_CONFIG}
    
    print(f"\n[+] BAT DAU CAO NANG CAP (8 CUM): {layer_name}")
    
    for start_index in range(0, total_features, page_size):
        params = {
            "service": "WFS",
            "version": "1.1.0",
            "request": "GetFeature",
            "typeName": layer_name,
            "outputFormat": "application/json",
            "maxFeatures": page_size,
            "startIndex": start_index
        }
        
        try:
            response = requests.get(base_url, params=params, timeout=180)
            if response.status_code == 200:
                features = response.json().get("features", [])
                for f in features:
                    # Giu nguyen 100% thuoc tinh
                    vung = get_vung_info(f.get('geometry'))
                    cluster_results[vung["id"]].append(f)
                
                print(f"   -> Da tai: {start_index + len(features)}/{total_features}...")
            else:
                print(f"   [!] Loi tai {start_index}: HTTP {response.status_code}")
        except Exception as e:
            print(f"   [!] Loi tai {start_index}: {str(e)}")
        
        time.sleep(0.3)

    # Luu 8 file cho moi lop (Line/Polygon)
    for v in VUNG_CONFIG:
        v_id = v["id"]
        v_features = cluster_results[v_id]
        if not v_features: continue
        
        filename = f"d:\\map-test\\FULL_{prefix}_vung_{v_id}.json"
        output = {
            "metadata": {
                "ten_vung": v["name"],
                "so_luong": len(v_features),
                "loai_du_lieu": prefix,
                "ghi_chu": "Du lieu 100% thuoc tinh va toa do goc tu Geoserver"
            },
            "type": "FeatureCollection",
            "features": v_features
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False)
        print(f"[OK] Da luu {len(v_features)} doi tuong vao {filename}")

if __name__ == "__main__":
    # 1. Cao Polygon (Dien tich nuoc)
    crawl_by_clusters("QuyHoachTL:SongSuoi_polygon", 6000, "polygon")
    
    # 2. Cao Line (Mang luoi song)
    crawl_by_clusters("QuyHoachTL:SongSuoi_line", 250333, "line")
