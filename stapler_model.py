import cadquery as cq
import os

# 📂 Set output folder (change this to your preferred location)
output_folder = "stapler_parts"
os.makedirs(output_folder, exist_ok=True)

# 📏 Dimensions (in mm, approx.)
length = 100
width = 30
height = 45

# --- Top Cover (spring-loaded arm) ---
top_cover = (
    cq.Workplane("XY")
    .box(length, width, height/3)
    .edges("|Z").fillet(5)
    .translate((0, 0, height/3))   # move it above base
)

# --- Base ---
base = (
    cq.Workplane("XY")
    .box(length, width, height/4)
    .edges("|Z").fillet(3)
    .translate((0, 0, -height/4))
)

# --- Staple Cartridge ---
cartridge = (
    cq.Workplane("XY")
    .box(length*0.8, width*0.6, height/8)
    .translate((0, 0, -height/6))
)

# --- Spring (simplified cylinder placeholder) ---
spring = (
    cq.Workplane("XY")
    .circle(width/6)
    .extrude(height/2)
    .translate((0, 0, 0))
)

# --- Export each part as STEP ---
cq.exporters.export(top_cover, os.path.join(output_folder, "stapler_top_cover.step"))
cq.exporters.export(base, os.path.join(output_folder, "stapler_base.step"))
cq.exporters.export(cartridge, os.path.join(output_folder, "stapler_cartridge.step"))
cq.exporters.export(spring, os.path.join(output_folder, "stapler_spring.step"))

print("✅ Stapler parts exported to:", os.path.abspath(output_folder))
