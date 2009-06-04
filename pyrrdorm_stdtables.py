#!/usr/bin/python

import pyrrdorm

class CpuTable(pyrrdorm.Table):
    @classmethod
    def TableName(self):
        return "CpuTable"

CpuTable.Derive("user", 0, 'U')
CpuTable.Derive("nice", 0, 'U')
CpuTable.Derive("sys", 0, 'U')
CpuTable.Derive("idle", 0, 'U')
CpuTable.Derive("iowait", 0, 'U')
CpuTable.Derive("irq", 0, 'U')
CpuTable.Derive("softirq", 0, 'U')
CpuTable.Avg(1, 4 * 60 * 24)

CpuTable.step = 15


class LoadTable(pyrrdorm.Table):
    @classmethod
    def TableName(self):
        return "LoadTable"

LoadTable.Gauge("l1", 0, 100)
LoadTable.Gauge("l5", 0, 100)
LoadTable.Gauge("l15", 0, 100)
LoadTable.Avg(1, 4 * 60 * 24)

LoadTable.step = 15


class TempTable(pyrrdorm.Table):
    @classmethod
    def TableName(self):
        return "TempTable"

TempTable.Gauge("cpu", 0, 100)
TempTable.Gauge("sys", 0, 100)
TempTable.Gauge("pcmcia", 0, 100)
TempTable.Gauge("gpu", 0, 100)
TempTable.Gauge("bat1", 0, 100)
TempTable.Gauge("bat2", 0, 100)
TempTable.Gauge("hdd", 0, 100)
TempTable.Gauge("fan", 0, 10000)
TempTable.Avg(1, 4 * 60 * 24)

TempTable.step = 15

class WirelessTable(pyrrdorm.Table):
    @classmethod
    def TableName(self):
        return "WirelessTable"

WirelessTable.Derive("inbytes", 0, 'U')
WirelessTable.Derive("outbytes", 0, 'U')
WirelessTable.Avg(1, 4 * 60 * 24)

WirelessTable.step = 15

class DiskstatsTable(pyrrdorm.Table):
    @classmethod
    def TableName(self):
        return "DiskstatsTable"

DiskstatsTable.Derive("readcnt", 0, 'U')
DiskstatsTable.Derive("readmerge", 0, 'U')
DiskstatsTable.Derive("readsectorcnt", 0, 'U')
DiskstatsTable.Derive("readmillis", 0, 'U')
DiskstatsTable.Derive("writecnt", 0, 'U')
DiskstatsTable.Derive("writemerge", 0, 'U')
DiskstatsTable.Derive("writesectorcnt", 0, 'U')
DiskstatsTable.Derive("writemillis", 0, 'U')
DiskstatsTable.Gauge("iosinprog", 0, 'U')
DiskstatsTable.Derive("iomillis", 0, 'U')
DiskstatsTable.Derive("ioweightedmillis", 0, 'U')
DiskstatsTable.Avg(1, 4 * 60 * 24)

DiskstatsTable.step = 15

class BatTable(pyrrdorm.Table):
    @classmethod
    def TableName(self):
        return "BatTable"

BatTable.Gauge("design_capacity", 0, 'U')
BatTable.Gauge("last_capacity", 0, 'U')
BatTable.Gauge("design_voltage", 0, 'U')
BatTable.Gauge("charge_rate", 0, 'U')
BatTable.Gauge("remaining_capacity", 0, 'U')
BatTable.Gauge("present_voltage", 0, 'U')
BatTable.Avg(1, 4 * 60 * 24)

BatTable.step = 15
