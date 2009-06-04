#!/usr/bin/python

import rrdtool

def loadgr(hours):
    rrdtool.graph('load' + str(hours) + '.png',
                  '--imgformat', 'PNG',
                  '--width', '800',
                  '--height', '600',
                  '--start', "now-" + str(60 * 60 * hours),
                  '--end', "now",
                  '--title', 'Load',
                  'DEF:l1=./system_data/LoadRow.rrd:l1:AVERAGE',
                  'DEF:l5=./system_data/LoadRow.rrd:l5:AVERAGE',
                  'DEF:l15=./system_data/LoadRow.rrd:l15:AVERAGE',
                  'LINE1:l1#0000FF:"L1"',
                  'LINE1:l5#00CCFF:"L5"',
                  'LINE1:l15#FF00FF:"L15"'
                  )

def tempgr(hours):
    rrdtool.graph('temp' + str(hours) + '.png',
                  '--imgformat', 'PNG',
                  '--width', '800',
                  '--height', '600',
                  '--start', "now-" + str(60 * 60 * hours),
                  '--end', "now",
                  '--title', 'Temperature',
                  'DEF:cpu=./system_data/TempRow.rrd:cpu:AVERAGE',
                  'DEF:sys=./system_data/TempRow.rrd:sys:AVERAGE',
                  'DEF:pcmcia=./system_data/TempRow.rrd:pcmcia:AVERAGE',
                  'DEF:gpu=./system_data/TempRow.rrd:gpu:AVERAGE',
                  'DEF:bat1=./system_data/TempRow.rrd:bat1:AVERAGE',
                  'DEF:bat2=./system_data/TempRow.rrd:bat2:AVERAGE',
                  'DEF:hdd=./system_data/TempRow.rrd:hdd:AVERAGE',
                  'DEF:fan=./system_data/TempRow.rrd:fan:AVERAGE',
                  'CDEF:f1=fan,0.02,*',
                  'LINE1:cpu#CBFE66:"cpu"',
                  'LINE1:sys#9AC346:"sys"',
                  'LINE1:pcmcia#00AB12:"pcmcia"',
                  'LINE1:gpu#6B7FD3:"gpu"',
                  'LINE1:bat1#FF00A3:"bat1"',
                  'LINE1:bat2#FFBB00:"bat2"',
                  'LINE1:hdd#FF8700:"hdd"',
                  'LINE1:f1#00CB33:"fan"',
                  )

def cpugr(hours):
    rrdtool.graph('cpu' + str(hours) + '.png',
                  '--imgformat', 'PNG',
                  '--width', '800',
                  '--height', '600',
                  '--start', "now-" + str(60 * 60 * hours),
                  '--end', "now",
                  '--title', 'Cpu',
                  'DEF:user=./system_data/CpuRow.rrd:user:AVERAGE',
                  'DEF:nice=./system_data/CpuRow.rrd:nice:AVERAGE',
                  'DEF:sys=./system_data/CpuRow.rrd:sys:AVERAGE',
                  'DEF:idle=./system_data/CpuRow.rrd:idle:AVERAGE',
                  'DEF:iowait=./system_data/CpuRow.rrd:iowait:AVERAGE',
                  'DEF:irq=./system_data/CpuRow.rrd:irq:AVERAGE',
                  'DEF:softirq=./system_data/CpuRow.rrd:softirq:AVERAGE',
                  'LINE1:user#CBFE66:"user"',
                  'LINE1:nice#9AC346:"nice"',
                  'LINE1:sys#00AB12:"sys"',
                  'LINE1:idle#6B7FD3:"idle"',
                  'LINE1:iowait#FF00A3:"iowait"',
                  'LINE1:irq#FFBB00:"irq"',
                  'LINE1:softirq#FF8700:"softirq"',
                  )

def wirelessgr(hours):
    rrdtool.graph('wireless' + str(hours) + '.png',
                  '--imgformat', 'PNG',
                  '--width', '800',
                  '--height', '600',
                  '--start', "now-" + str(60 * 60 * hours),
                  '--end', "now",
                  '--title', 'Wireless(ath0)',
                  'DEF:inbytes=./system_data/WirelessRow.rrd:inbytes:AVERAGE',
                  'DEF:outbytes=./system_data/WirelessRow.rrd:outbytes:AVERAGE',
                  'LINE2:inbytes#0000FF:"inbytes"',
                  'LINE2:outbytes#FF0000:"outbytes"',
                  )

def diskstatsgr(hours):
    rrdtool.graph('diskstats' + str(hours) + '.png',
                  '--imgformat', 'PNG',
                  '--width', '800',
                  '--height', '600',
                  '--start', "now-" + str(60 * 60 * hours),
                  '--end', "now",
                  '--title', 'Disk Stats',
                  'DEF:readcnt=./system_data/DiskstatsRow.rrd:readcnt:AVERAGE',
                  'DEF:readmerge=./system_data/DiskstatsRow.rrd:readmerge:AVERAGE',
                  'DEF:readsectorcnt=./system_data/DiskstatsRow.rrd:readsectorcnt:AVERAGE',
                  'DEF:readmillis=./system_data/DiskstatsRow.rrd:readmillis:AVERAGE',
                  'DEF:writecnt=./system_data/DiskstatsRow.rrd:writecnt:AVERAGE',
                  'DEF:writemerge=./system_data/DiskstatsRow.rrd:writemerge:AVERAGE',
                  'DEF:writesectorcnt=./system_data/DiskstatsRow.rrd:writesectorcnt:AVERAGE',
                  'DEF:writemillis=./system_data/DiskstatsRow.rrd:writemillis:AVERAGE',
                  'DEF:iosinprog=./system_data/DiskstatsRow.rrd:iosinprog:AVERAGE',
                  'DEF:iomillis=./system_data/DiskstatsRow.rrd:iomillis:AVERAGE',
                  'DEF:ioweightedmillis=./system_data/DiskstatsRow.rrd:ioweightedmillis:AVERAGE',
                  'LINE1:readcnt#CBFE66:"readcnt"',
                  'LINE1:readmerge#9AC346:"readmerge"',
                  'LINE1:readsectorcnt#00AB12:"readsectorcnt"',
                  'LINE1:readmillis#6B7FD3:"readmillis"',
                  'LINE1:writecnt#FF00A3:"writecnt"',
                  'LINE1:writemerge#FFBB00:"writemerge"',
                  'LINE1:writesectorcnt#FF8700:"wrtiesectorcnt"',
                  'LINE1:writemillis#00CB33:"writemillis"',
                  'LINE1:iosinprog#CBFE66:"iosinprog"',
                  'LINE1:iomillis#9AC346:"iomillis"',
                  'LINE1:ioweightedmillis#00AB12:"ioweightedmillis"',
                  )

def batgr(hours):
    rrdtool.graph('bat' + str(hours) + '.png',
                  '--imgformat', 'PNG',
                  '--width', '800',
                  '--height', '600',
                  '--start', "now-" + str(60 * 60 * hours),
                  '--end', "now",
                  '--title', 'Battery Stats',
                  'DEF:last_capacity=./system_data/BatRow.rrd:last_capacity:AVERAGE',
                  'DEF:design_voltage=./system_data/BatRow.rrd:design_voltage:AVERAGE',
                  'DEF:charge_rate=./system_data/BatRow.rrd:charge_rate:AVERAGE',
                  'DEF:remaining_capacity=./system_data/BatRow.rrd:remaining_capacity:AVERAGE',
                  'DEF:present_voltage=./system_data/BatRow.rrd:present_voltage:AVERAGE',
                  'LINE1:last_capacity#9AC346:"last_capacity"',
                  'LINE1:design_voltage#00AB12:"design_voltage"',
                  'LINE1:remaining_capacity#6B7FD3:"remaining_capacity"',
                  'LINE1:present_voltage#FF00A3:"present_voltage"',
                  )

if __name__ == '__main__':
    loadgr(1)
    loadgr(4)
    loadgr(12)
    loadgr(24)
    tempgr(1)
    tempgr(4)
    tempgr(12)
    tempgr(24)
    cpugr(1)
    cpugr(4)
    cpugr(12)
    cpugr(24)
    wirelessgr(1)
    wirelessgr(4)
    wirelessgr(12)
    wirelessgr(24)
    diskstatsgr(1)
    diskstatsgr(4)
    diskstatsgr(12)
    diskstatsgr(24)
    batgr(1)
    batgr(4)
    batgr(12)
    batgr(24)
