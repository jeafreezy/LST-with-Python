#Installing the libraries

library(raster)
require(ncdf4)
require(rgdal)

## Input: a netCDF file
file.nc <- "C:/LEARNING(2020)/RESEARCH_WORK/data/NTL/VNP02DNB_NRT.A2020057.1242.001.nc"

## Output: a GeoTIFF file
file.tiff <- 'C:/LEARNING(2020)/RESEARCH_WORK/data/NTL/nt2.tiff'

## Import netCDF
r.rain <- raster(file.nc)

## Save to disk as GeoTIFF
writeRaster(r.rain, filename = file.tiff, format = 'GTiff',options="INTERLEAVE=BAND", overwrite = TRUE)


