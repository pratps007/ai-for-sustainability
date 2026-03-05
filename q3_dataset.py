import os
import pandas as pd

# load labels created in Q2
labels = pd.read_csv("tile_labels.csv")

image_folder = "data/rgb"

dataset = []

for img in os.listdir(image_folder):

    if img.endswith(".png"):

        name = img.replace(".png","")
        parts = name.split("_")

        lat = float(parts[0])
        lon = float(parts[1])

        dataset.append([img, lat, lon])

df = pd.DataFrame(dataset, columns=["image", "lat", "lon"])

print(df.head())

df.to_csv("dataset.csv", index=False)