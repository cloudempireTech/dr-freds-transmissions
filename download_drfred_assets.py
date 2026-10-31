import os
import urllib.request
from PIL import Image

def download_and_optimize():
    img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\dr-freds-transmissions\assets\images"
    os.makedirs(img_dir, exist_ok=True)

    images = [
        # 1. Transmission rebuild on mechanic workbench
        ("transmission-rebuild-bench.jpg", "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=1200&q=80"),
        # 2. Computerized auto diagnostic scanner
        ("computer-diagnostic-scan.jpg", "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80"),
        # 3. Precision automotive gears / torque converter assembly
        ("torque-converter-assembly.jpg", "https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=1200&q=80"),
        # 4. Fluid maintenance / transmission ATF service
        ("transmission-fluid-flush.jpg", "https://images.unsplash.com/photo-1486006920555-c77dce18193b?auto=format&fit=crop&w=1200&q=80"),
        # 5. Mechanic under hydraulic lift
        ("mechanic-under-vehicle-lift.jpg", "https://images.unsplash.com/photo-1613214149922-f1809c99b414?auto=format&fit=crop&w=1200&q=80"),
        # 6. Drivetrain & differential gears
        ("transfer-case-differential.jpg", "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=1200&q=80"),
        # 7. Flatbed emergency towing
        ("towing-service-truck.jpg", "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=1200&q=80"),
        # 8. Heavy clutch / manual transmission parts
        ("clutch-pressure-plate.jpg", "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=1200&q=80"),
        # 9. Solenoid / TCM precision electronics
        ("transmission-valve-body.jpg", "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80"),
        # 10. Key handoff / customer warranty trust
        ("shop-warranty-handshake.jpg", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80")
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for name, url in images:
        out_path = os.path.join(img_dir, name)
        temp_path = os.path.join(img_dir, "temp_" + name)
        print(f"Downloading {name}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp, open(temp_path, 'wb') as out_file:
                out_file.write(resp.read())

            with Image.open(temp_path) as im:
                im = im.convert("RGB")
                im = im.resize((1200, 800), Image.Resampling.LANCZOS)
                im.save(out_path, "JPEG", quality=82, optimize=True)

            if os.path.exists(temp_path):
                os.remove(temp_path)

            file_size_kb = os.path.getsize(out_path) / 1024
            print(f"  Saved {name} ({file_size_kb:.1f} KB)")
        except Exception as e:
            print(f"  Error downloading {name}: {e}")

if __name__ == "__main__":
    download_and_optimize()
