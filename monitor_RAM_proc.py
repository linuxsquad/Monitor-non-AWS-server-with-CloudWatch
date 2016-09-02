#!/usr/bin/env python

import os
import psutil
import json
import time
import datetime

def monitor_RAMproc( procName = 'httpd'):
    with open("/var/tmp/aws_monitor_ramproc.log", "a") as logFile:
        ram = psutil.virtual_memory()

        stat = 0
        for proc in psutil.process_iter():
            if proc.name == procName:
                stat += 1

        logFile.write(str(json.dumps({'timestamp' : str(datetime.datetime.now()), 'ramFreePrcnt' : int(100 * float(ram.free) / float(ram.total)), procName+'ProcRunning' : (stat) }))+"\n")

def run_monitor(sampleTime = 30):
    while True:
        monitor_RAMproc("httpd")
        time.sleep(sampleTime)

if __name__ == "__main__":
    run_monitor(60)
