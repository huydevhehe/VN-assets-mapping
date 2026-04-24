import requests
import json
import time
import os

def simplify_geometry(geometry, precision=5):
    """Lam tron toa do de giam dung luong file"""
    if not geometry:
        return geometry
    
    def round_coords(coords):
        if isinstance(coords[0], (int, float)):
            return [round(c, precision) for c in coords]
        return [round_coords(c) for c in coords]

    geometry['coordinates'] = round_coords(geometry['coordinates'])
    return geometry

def get_region(geometry):
    """Phan loai mien dua tren vi do (Latitude)"""
    try:
        coords = geometry['coordinates']
        # Lay mot diem dai dien (diem dau tien)
        while isinstance(coords[0], list):
            coords = coords[0]
        
        lat = coords[1]
        if lat > 19.5:
            return "bac"
        elif lat > 11.5:
            return "trung"
        else:
            return "nam"
    except:
        return "bac" # Mac dinh neu co loi

def crawl_and_split(layer_name, total_features, prefix):
    base_url = "http://bando.quyhoachthuyloi.vn/geoserver/wfs"
    page_size = 2000
    
    results = {
        "bac": [],
        "trung": [],
        "nam": []
    }
    
    print(f"\n[+] Bat dau cao lop: {layer_name}")
    
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
            response = requests.get(base_url, params=params, timeout=60)
            if response.status_code == 200:
                data = response.json()
                features = data.get("features", [])
                
                for f in features:
                    # 1. Toi uu hoa hinh hoc
                    f['geometry'] = simplify_geometry(f.get('geometry'))
                    
                    # 2. Loc thuoc tinh
                    props = f.get("properties", {})
                    f["properties"] = {
                        "ten": props.get("ten") or props.get("ten_song") or props.get("diadanh"),
                        "loai": props.get("loaisong") or props.get("loai_song"),
                        "id": props.get("objectid")
                    }
                    
                    # 3. Phan mien
                    region = get_region(f.get('geometry'))
                    results[region].append(f)
                
                print(f"   -> Da tai: {start_index + len(features)}/{total_features}...")
            else:
                print(f"   [!] Loi tai {start_index}: HTTP {response.status_code}")
        except Exception as e:
            print(f"   [!] Loi tai {start_index}: {str(e)}")
        
        time.sleep(0.2)

    # Luu cac file theo mien
    for region in ["bac", "trung", "nam"]:
        filename = f"d:\\map-test\\song_{prefix}_{region}.json"
        output = {
            "type": "FeatureCollection",
            "features": results[region]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False)
        print(f"[OK] Da luu {len(results[region])} doi tuong vao {filename}")

if __name__ == "__main__":
    # 1. Cao Polygon (5.697)
    crawl_and_split("QuyHoachTL:SongSuoi_polygon", 6000, "polygon")
    
    # 2. Cao Line (250.333)
    # De dam bao an toan cho server va may ban, toi se cao theo cac dot
    crawl_and_split("QuyHoachTL:SongSuoi_line", 250333, "line")
