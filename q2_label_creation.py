import rasterio
import numpy as np
from scipy.stats import mode
import pandas as pd

raster = rasterio.open("data/worldcover_bbox_delhi_ncr_2021.tif")

print("Raster CRS:", raster.crs)

band = raster.read(1)

print("Raster shape:", band.shape)
print("Unique classes:", np.unique(band))
tile_size = 256
labels = []

for i in range(0, band.shape[0], tile_size):
    for j in range(0, band.shape[1], tile_size):

        tile = band[i:i+tile_size, j:j+tile_size]

        if tile.size == 0:
            continue

        m = mode(tile, axis=None, keepdims=False)
        dominant_class = int(m.mode)

        labels.append([i, j, dominant_class])

df = pd.DataFrame(labels, columns=["row", "col", "label"])

print(df.head())
print("Total tiles:", len(df))
df.to_csv("tile_labels.csv", index=False)
df.to_csv("tile_labels.csv", index=False)