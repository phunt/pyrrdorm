from __future__ import with_statement

from pyrrdorm_stdtables import *

from subprocess import Popen, PIPE
import re

class ProcCpuTable(CpuTable):
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

class ProcLoadTable(LoadTable):
    def __init__(self):
        with open('/proc/loadavg', 'r') as f:
            line = f.readline()
        d = line.split(' ')
        self.l1 = d[0]
        self.l5 = d[1]
        self.l15 = d[2]


class ProcTempTable(TempTable):
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

class ProcWirelessTable(WirelessTable):
    def __init__(self):
        ath0 = Popen(['grep', 'ath0', '/proc/net/dev'], stdout=PIPE)
        line = ath0.communicate()[0]

        d = line.split()
        self.inbytes  = d[0].split(':')[1]
        self.outbytes = d[8]

class ProcDiskstatsTable(DiskstatsTable):
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

class ProcBatTable(BatTable):
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
