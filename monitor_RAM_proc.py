#!/usr/bin/env python
#
#

import os
import psutil
import json
import time
import datetime
import subprocess

LOGFILE = "/var/tmp/aws_monitor_ramhttpd.log"

def monitor_RAMproc( procName = 'httpd'):
    cpuinfo = psutil.cpu_times_percent()
    ram = psutil.virtual_memory()

    stat = 0
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            if pinfo['name'] == procName:
                stat += 1
        except psutil.NoSuchProcess:
            pass

    with open(LOGFILE, "w") as logFile:
        logFile.seek(0)
        logFile.truncate()
        logFile.write("[ "+str(json.dumps({'MetricName': 'ramFreePrcnt', 'Value' : int(100 * float(ram.free) / float(ram.total)) }))+",\n "+str(json.dumps({'MetricName': procName+'-ProcRunning', 'Value' : int(stat) }))+",\n "+str(json.dumps({'MetricName': 'CpuSteal', 'Value' : cpuinfo.steal }))+",\n "+str(json.dumps({'MetricName': 'CpuIdle', 'Value' : cpuinfo.idle }))+",\n "+str(json.dumps({'MetricName': 'CpuUser', 'Value' : cpuinfo.user }))+",\n "+str(json.dumps({'MetricName': 'CpuSystem', 'Value' : cpuinfo.system }))+",\n "+str(json.dumps({'MetricName': 'CpuUtil', 'Value' : psutil.cpu_percent() }))+" ] \n")
        
    awsBashCommand = "aws cloudwatch put-metric-data --namespace gooseHTTP --metric-data file://"+LOGFILE
    process = subprocess.Popen(awsBashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def run_monitor(sampleTime = 30):
    while True:
        monitor_RAMproc("httpd")
        time.sleep(sampleTime)

if __name__ == "__main__":
    run_monitor(60)
