#!/usr/bin/env python3.6
"""
 * Copyright (c) 2019 Rodrigo Osorio <rodrigo@osorio.me>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer
 *    in this position and unchanged.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import math
import datetime
import time
import json
import sys, getopt
import signal
from geographiclib.geodesic import Geodesic


class Navigation():
    _KMPH2KMPS = 0.277778

    def __init__(self, geofile, speed, loop):
        with open(geofile, 'r') as jsonfile:
            data = json.load(jsonfile)
        self.journey = data['features'][0]['geometry']['coordinates']
        self.speed = int(speed)
        self.loop = loop
        self.status = None

        # recover the first position in the list
        self.curr_pos = (self.journey[0][0],self.journey[0][1])

    def do_run(self):
        geod = Geodesic.WGS84
        loop = True
        
        while (loop):
            prev = None
            for step in self.journey:
                if (prev):
                    g = geod.Inverse(prev[0], prev[1], step[0], step[1]);
                    l = geod.InverseLine(prev[0], prev[1], step[0], step[1])
                    interval = self.speed * self._KMPH2KMPS
                    istep = int(math.ceil(l.s13 / interval))

                    # Calculate heading
                    y = (math.radians(prev[0]), math.radians(step[0]))
                    x = (math.radians(prev[1]), math.radians(step[1]))

                    delta = y[1] - y[0]
                    heady = math.cos(x[1]) * math.sin(delta)
                    headx = math.cos(x[0]) * math.sin(x[1]) - math.sin(x[0]) * math.cos(x[1]) * math.cos(delta)
                    heading = math.degrees(math.atan2(heady, headx))

                    for i in range (istep + 1):
                        s = min(interval * i, l.s13)
                        loc = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)

                        print ("dist {:.0f} meters  lat {:.5f} long {:.5f} heading {:.5f}".format(
                            loc['s12'], loc['lat2'], loc['lon2'], heading))
                        time.sleep(1)
                prev = step;
            loop = self.loop


    def dump_journey(self):
        for step in self.journey:
            print("Step {} : {}".format(c, step))
            c+=1

def handler(signum, frame):
    print("Au revoir monde cruel")
    sys.exit(0)


if __name__ == "__main__":
    do_loop = False
    geofile =''
    speed = 0

    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:s:l",["file=","speed="])
    except getopt.GetoptError:
        print ('navigate.py -f <geoJSON> -s <speed> [-l]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-l':
            do_loop = True
        elif opt in ('-s', '-speed'):
            speed = arg
        elif opt in ('-f', '-file'):
            geofile = arg

    signal.signal(signal.SIGINT, handler)

    nav = Navigation(geofile, speed,do_loop)
    nav.do_run()

