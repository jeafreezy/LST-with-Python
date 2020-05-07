#Installing the libraries

library(raster)
require(ncdf4)
require(rgdal)

## Input: a netCDF file
file.nc <- "C:\\LEARNING(2020)\\RESEARCH_WORK\\data\\NTL\\New_Study_Area\\VNP02DNB_NRT.A2020095.0130.001.nc" 


#That is a file path--> It point the program to the location of the file you want to work wit

## Output: a GeoTIFF file
file.tiff <- 'C:/LEARNING(2020)/RESEARCH_WORK/data/NTL/New_Study_Area/VNP02DNB_NRT1.tif'

## Import netCDF
r.rain <- raster(file.nc)

## Save to disk as GeoTIFF
writeRaster(r.rain, filename = file.tiff, format = 'GTiff',options="INTERLEAVE=BAND", overwrite = TRUE)


