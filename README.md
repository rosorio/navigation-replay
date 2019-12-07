# navigation-replay

A tool to helps you to generate fake position and heading for a device based on a pre-recorded track.

# Installation

This script was writen for and tested with python3+ and requere the following dependencies:

* geographiclib.geodesic library (geographiclib package in FreeBSD)

# Run

  ./navigate.py -f GeoJSON-file -s speed-in-kmph [-l]

* -f : the argument is a GPS track in GeoJson format
* -s : the argument is the speed in Km/h (100 for 100 Km per hour)
* -l : nor argmenet, optional. Loop over and over the same dataset 

# GeoJSON format

The [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) format is a format for encoding a variety of geographic data structures defined by the RFC 7946.

You can generate your own track or convert formats from the folowing websites :

* http://share.mapbbcode.org/
* http://geojson.io/
* https://github.com/tmcw/awesome-geojson
