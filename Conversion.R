#Installing the libraries

library(raster)
require(ncdf4)

## Input: a netCDF file
file.nc <- "C:/LEARNING(2020)/RESEARCH_WORK/data/NTL/ntl.nc"

## Output: a GeoTIFF file
file.tiff <- 'C:/LEARNING(2020)/RESEARCH_WORK/data/NTL/ntl.tiff'

## Import netCDF
r.night_light_imagery <- raster(file.nc)

## Save to disk as GeoTIFF
writeRaster(night_light_imagery, filename = file.tiff, format = 'GTiff', overwrite = T)


