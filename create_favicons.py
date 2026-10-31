import os
from PIL import Image, ImageDraw

def generate_icons():
    img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\dr-freds-transmissions\assets\images"
    os.makedirs(img_dir, exist_ok=True)

    # 1. logo.svg
    svg_logo = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 90" width="460" height="90">
  <defs>
    <linearGradient id="gearGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF3B30"/>
      <stop offset="100%" stop-color="#FF9500"/>
    </linearGradient>
  </defs>
  <!-- Transmission Gear & Torque Emblem -->
  <rect x="6" y="8" width="74" height="74" rx="16" fill="#0B0F19" stroke="url(#gearGrad)" stroke-width="2.5"/>
  <circle cx="43" cy="45" r="22" fill="none" stroke="url(#gearGrad)" stroke-width="5" stroke-dasharray="10,4"/>
  <circle cx="43" cy="45" r="9" fill="#FF3B30"/>
  <circle cx="43" cy="45" r="4" fill="#FFFFFF"/>
  
  <!-- Text Brand -->
  <text x="96" y="44" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-weight="900" font-size="27" fill="#FFFFFF" letter-spacing="1">DR. FRED'S TRANSMISSIONS</text>
  <text x="96" y="68" font-family="'Inter', system-ui, sans-serif" font-weight="700" font-size="11.5" fill="#FF9500" letter-spacing="3">SPRING, TEXAS &bull; ATRA CERTIFIED</text>
</svg>"""

    with open(os.path.join(img_dir, "logo.svg"), "w", encoding="utf-8") as f:
        f.write(svg_logo)

    # 2. favicon.svg
    svg_favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="favGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF3B30"/>
      <stop offset="100%" stop-color="#FF9500"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="24" fill="#0B0F19"/>
  <rect x="6" y="6" width="88" height="88" rx="20" fill="none" stroke="url(#favGrad)" stroke-width="4"/>
  <circle cx="50" cy="50" r="26" fill="none" stroke="url(#favGrad)" stroke-width="6" stroke-dasharray="12,5"/>
  <circle cx="50" cy="50" r="11" fill="#FF3B30"/>
  <circle cx="50" cy="50" r="4" fill="#FFFFFF"/>
</svg>"""

    with open(os.path.join(img_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg_favicon)

    # 512x512 image
    size = (512, 512)
    img = Image.new("RGBA", size, (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([(16, 16), (496, 496)], radius=96, outline=(255, 59, 48, 255), width=16)
    
    # Outer gear ring
    draw.ellipse([(140, 140), (372, 372)], outline=(255, 149, 0, 255), width=28)
    draw.ellipse([(206, 206), (306, 306)], fill=(255, 59, 48, 255))
    draw.ellipse([(236, 236), (276, 276)], fill=(255, 255, 255, 255))

    img.save(os.path.join(img_dir, "logo-512.png"), "PNG")

    apple = img.resize((180, 180), Image.Resampling.LANCZOS)
    apple.save(os.path.join(img_dir, "apple-touch-icon.png"), "PNG")

    fav32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    fav32.save(os.path.join(img_dir, "favicon-32x32.png"), "PNG")
    fav32.save(os.path.join(img_dir, "favicon.ico"), format="ICO", sizes=[(32, 32)])

    print("Dr. Fred's Transmissions favicon suite generated successfully!")

if __name__ == "__main__":
    generate_icons()
