import geopandas as gpd
import matplotlib.pyplot as plt

# Load Delhi NCR region (geojson)
gdf = gpd.read_file("data/delhi_ncr_region.geojson")

print("CRS:", gdf.crs)

# Plot
gdf.plot(edgecolor='black', facecolor='none')
plt.title("Delhi NCR Boundary")
plt.show()
