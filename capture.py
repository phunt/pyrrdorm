#!/usr/bin/python

from __future__ import with_statement

import pyrrdorm
from subprocess import Popen, PIPE
import re

class CpuRow(pyrrdorm.Row):
    ds = []
    rra = []
    def __init__(self):
        with open('/proc/stat', 'r') as f:
            line = f.readline()
        d = line.split(' ')
        self.user    = d[1]
        self.nice    = d[2]
        self.sys     = d[3]
        self.idle    = d[4]
        self.iowait  = d[5]
        self.irq     = d[6]
        self.softirq = d[7]

#TODO use metaclasses instead?
CpuRow.Derive("user", 0, 'U')
CpuRow.Derive("nice", 0, 'U')
CpuRow.Derive("sys", 0, 'U')
CpuRow.Derive("idle", 0, 'U')
CpuRow.Derive("iowait", 0, 'U')
CpuRow.Derive("irq", 0, 'U')
CpuRow.Derive("softirq", 0, 'U')
CpuRow.Avg(1, 4 * 60 * 24)

CpuRow.step = 15


class LoadRow(pyrrdorm.Row):
    ds = []
    rra = []
    def __init__(self):
        with open('/proc/loadavg', 'r') as f:
            line = f.readline()
        d = line.split(' ')
        self.l1 = d[0]
        self.l5 = d[1]
        self.l15 = d[2]

#TODO use metaclasses instead?
LoadRow.Gauge("l1", 0, 100)
LoadRow.Gauge("l5", 0, 100)
LoadRow.Gauge("l15", 0, 100)
LoadRow.Avg(1, 4 * 60 * 24)

LoadRow.step = 15


class TempRow(pyrrdorm.Row):
    ds = []
    rra = []
    def __init__(self):
        with open('/proc/acpi/ibm/thermal', 'r') as f:
            line = f.readline()
        d = line[14:].split(' ')
        self.cpu    = d[0]
        self.sys    = d[1]
        self.pcmcia = d[2]
        self.gpu    = d[3]
        self.bat1   = d[4]
        self.bat2   = d[6]

        nc = Popen(['nc', 'localhost', '7634'], stdout=PIPE)
        line = nc.communicate()[0]

        self.hdd = line.split('|')[3]

        with open('/proc/acpi/ibm/fan', 'r') as f:
            f.readline()
            line = f.readline()

        m = re.search(r'\d+', line)
        if m:
            self.fan = m.group()
        else:
            self.fan = 'U'

#TODO use metaclasses instead?
TempRow.Gauge("cpu", 0, 100)
TempRow.Gauge("sys", 0, 100)
TempRow.Gauge("pcmcia", 0, 100)
TempRow.Gauge("gpu", 0, 100)
TempRow.Gauge("bat1", 0, 100)
TempRow.Gauge("bat2", 0, 100)
TempRow.Gauge("hdd", 0, 100)
TempRow.Gauge("fan", 0, 10000)
TempRow.Avg(1, 4 * 60 * 24)

TempRow.step = 15

class WirelessRow(pyrrdorm.Row):
    ds = []
    rra = []
    def __init__(self):
        ath0 = Popen(['grep', 'ath0', '/proc/net/dev'], stdout=PIPE)
        line = ath0.communicate()[0]

        d = line.split()
        self.inbytes  = d[0].split(':')[1]
        self.outbytes = d[8]

#TODO use metaclasses instead?
WirelessRow.Derive("inbytes", 0, 'U')
WirelessRow.Derive("outbytes", 0, 'U')
WirelessRow.Avg(1, 4 * 60 * 24)

WirelessRow.step = 15

class DiskstatsRow(pyrrdorm.Row):
    ds = []
    rra = []
    def __init__(self):
        ds = Popen(['grep', 'sda2', '/proc/diskstats'], stdout=PIPE)
        line = ds.communicate()[0]

        d = line.split()
        self.readcnt  = d[3]
        self.readmerge = d[4]
        self.readsectorcnt = d[5]
        self.readmillis = d[6]
        self.writecnt = d[7]
        self.writemerge = d[8]
        self.writesectorcnt = d[9]
        self.writemillis = d[10]
        self.iosinprog = d[11]
        self.iomillis = d[12]
        self.ioweightedmillis = d[13]

#TODO use metaclasses instead?
DiskstatsRow.Derive("readcnt", 0, 'U')
DiskstatsRow.Derive("readmerge", 0, 'U')
DiskstatsRow.Derive("readsectorcnt", 0, 'U')
DiskstatsRow.Derive("readmillis", 0, 'U')
DiskstatsRow.Derive("writecnt", 0, 'U')
DiskstatsRow.Derive("writemerge", 0, 'U')
DiskstatsRow.Derive("writesectorcnt", 0, 'U')
DiskstatsRow.Derive("writemillis", 0, 'U')
DiskstatsRow.Gauge("iosinprog", 0, 'U')
DiskstatsRow.Derive("iomillis", 0, 'U')
DiskstatsRow.Derive("ioweightedmillis", 0, 'U')
DiskstatsRow.Avg(1, 4 * 60 * 24)

DiskstatsRow.step = 15

class BatRow(pyrrdorm.Row):
    ds = []
    rra = []
    def __init__(self):
        with open('/proc/acpi/battery/BAT0/info', 'r') as f:
            f.readline()
            m = re.search(r'\d+', f.readline())
            self.design_capacity = m.group()
            m = re.search(r'\d+', f.readline())
            self.last_capacity = m.group()
            f.readline()
            m = re.search(r'\d+', f.readline())
            self.design_voltage = m.group()

        with open('/proc/acpi/battery/BAT0/state', 'r') as f:
            f.readline()
            f.readline()
            f.readline()
            m = re.search(r'\d+', f.readline())
            self.charge_rate = m.group()
            m = re.search(r'\d+', f.readline())
            self.remaining_capacity = m.group()
            m = re.search(r'\d+', f.readline())
            self.present_voltage = m.group()

#TODO use metaclasses instead?
BatRow.Gauge("design_capacity", 0, 'U')
BatRow.Gauge("last_capacity", 0, 'U')
BatRow.Gauge("design_voltage", 0, 'U')
BatRow.Gauge("charge_rate", 0, 'U')
BatRow.Gauge("remaining_capacity", 0, 'U')
BatRow.Gauge("present_voltage", 0, 'U')
BatRow.Avg(1, 4 * 60 * 24)

BatRow.step = 15


if __name__ == '__main__':
    pyrrdorm.add(LoadRow)
    pyrrdorm.add(TempRow)
    pyrrdorm.add(CpuRow)
    pyrrdorm.add(WirelessRow)
    pyrrdorm.add(DiskstatsRow)
    pyrrdorm.add(BatRow)
    pyrrdorm.run("./system_data")
