# Geodesignhub NLCD Evaluation Maps Builder
This program uses CORINE landcover data from [Multi Resolution Land Characteristics Consortium (MLRC)](https://www.mrlc.gov/) to develop Evaluation maps for [Geodesignhub](https://www.geodesignhub.com/). It uses simple rules to parse the existing data and build evaluation maps that can be used directly on Geodesignhub. NLCD data is available only for mainland United States so this tool can be used to make evaluation maps only for sites in the US.

Making evaluation maps is the most time consuming part of a Geodesign study, using this script it can be automated. The following evaluation maps are generated: 

* Urban (URB / HSG + COM)
* Agriculture (AG)
* Industrial (IND)
* Forests (FOR)
* Hydrology (HYDRO)

Find out more about evaluation maps at the [Making Evaluations Maps](https://community.geodesignhub.com/t/making-evaluation-maps/62) in our community page. 

If you are new to Geodesignhub, please see our course at [Teachable.com](https://geodesignhub.teachable.com/p/geodesign-with-geodesignhub/)  

## Installation
Use the requirements.txt file to install libraries that are required for the program

```
pip install -r requirements.txt
```

## 3-Step process
**1. Download raw data**

1. Go to [Multi Resolution Land Characteristics Consortium (MLRC)](https://www.mrlc.gov/) to order and download the NCLD raster data and clip it to your area of interest.
2. Convert the clipped area to Vector by using the `Polygonize` command for e.g. in QGIS
2. Put this file in the ```working``` folder
3. Update the ```config.py``` file to show 

**2. Update config.py**

1. Set the boundary parameter to set the bounding box co-ordinates in `(southwest_lng,southwest_lat,northeast_lng,northeast_lat)` format. 

**3. Upload Evaluations**

1. Run the `NLCD-evaluations-generator.py` script and check the `output` folder for the Evaluation GeoJSON that can be uploaded to Geodesignhub

