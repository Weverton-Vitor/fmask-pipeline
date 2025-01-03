import ee
import os
from utils import donwload_images

ee.Authenticate()
ee.Initialize(project="ee-cloud-segmentation")

# start = ee.Date("2017-01-01")
start = "2020-11-30"
finish = "2024-12-30"
collection_id = "COPERNICUS/S2_HARMONIZED"


shapefiles_path = "./shapefiles/"

shapefiles = [
    f"{shapefiles_path}{shapefile}"
    for shapefile in os.listdir(shapefiles_path)
    if ".zip" in shapefile
]

for shapefile in shapefiles:
    donwload_images(
        collection_id=collection_id,
        dowload_path="./sentinel_scenes/",
        init_date=start,
        final_date=finish,
        roi_path=shapefile,
        all_bands=False,
        prefix_images_name=f"sentinel2_6B_TOA_{shapefile.split('/')[-1].replace('.zip', '')}",
    )
