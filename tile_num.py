#!/usr/bin/python
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('lat', type=float)
parser.add_argument('lon', type=float)
parser.add_argument('zoom', type=int)
args = parser.parse_args()
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

tile = deg2num(args.lat,args.lon,args.zoom)
print('/osm_tiles/'+str(args.zoom)+'/'+str(tile[0])+'/'+str(tile[1])+'.png')
