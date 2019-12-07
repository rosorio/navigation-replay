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

```
% ./navigate.py -f sample.geojson -s 5000
dist 0 meters  lat 2.32910 long 48.85749 heading 74.31880
dist 1389 meters  lat 2.34145 long 48.85976 heading 74.31880
dist 2778 meters  lat 2.35380 long 48.86202 heading 74.31880
dist 4167 meters  lat 2.36616 long 48.86429 heading 74.31880
dist 5556 meters  lat 2.37851 long 48.86656 heading 74.31880
dist 6944 meters  lat 2.39086 long 48.86882 heading 74.31880
dist 8333 meters  lat 2.40321 long 48.87109 heading 74.31880
dist 9722 meters  lat 2.41556 long 48.87336 heading 74.31880
dist 11111 meters  lat 2.42791 long 48.87562 heading 74.31880
dist 12500 meters  lat 2.44027 long 48.87789 heading 74.31880
dist 13889 meters  lat 2.45262 long 48.88016 heading 74.31880
dist 15278 meters  lat 2.46497 long 48.88242 heading 74.31880
dist 16667 meters  lat 2.47732 long 48.88469 heading 74.31880
dist 18056 meters  lat 2.48967 long 48.88696 heading 74.31880
dist 19444 meters  lat 2.50203 long 48.88922 heading 74.31880
dist 20833 meters  lat 2.51438 long 48.89149 heading 74.31880
dist 22222 meters  lat 2.52673 long 48.89376 heading 74.31880
dist 23611 meters  lat 2.53908 long 48.89603 heading 74.31880
dist 25000 meters  lat 2.55143 long 48.89829 heading 74.31880
dist 26389 meters  lat 2.56378 long 48.90056 heading 74.31880
dist 26560 meters  lat 2.56531 long 48.90084 heading 74.31880
dist 0 meters  lat 2.56531 long 48.90084 heading 81.75373        <--- Reach second point
dist 1389 meters  lat 2.57781 long 48.90201 heading 81.75373
dist 2778 meters  lat 2.59032 long 48.90319 heading 81.75373
```

# GeoJSON format

The [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) format is a format for encoding a variety of geographic data structures defined by the RFC 7946.

You can generate your own track or convert formats from the folowing websites :

* http://share.mapbbcode.org/
* http://geojson.io/
* https://github.com/tmcw/awesome-geojson
