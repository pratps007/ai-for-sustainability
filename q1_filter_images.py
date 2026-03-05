import geopandas as gpd
from shapely.geometry import Point
import os

# load Delhi NCR boundary
gdf = gpd.read_file("data/delhi_ncr_region.geojson")

# read all satellite images
image_folder = "data/rgb"
image_files = os.listdir(image_folder)

print("Total images:", len(image_files))

filtered_images = []

for img in image_files:

    # remove .png
    name = img.replace(".png", "")

    # split filename to get coordinates
    parts = name.split("_")

    lat = float(parts[0])
    lon = float(parts[1])

    point = Point(lon, lat)

    # check if point lies inside NCR
    if gdf.contains(point).any():
        filtered_images.append(img)

print("Images inside NCR:", len(filtered_images))
print("Percentage inside NCR:", len(filtered_images)/len(image_files)*100)