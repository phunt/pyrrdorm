#!/usr/bin/python

from proc_impl import *

if __name__ == '__main__':
    pyrrdorm.add(ProcLoadTable)
    pyrrdorm.add(ProcTempTable)
    pyrrdorm.add(ProcCpuTable)
    pyrrdorm.add(ProcWirelessTable)
    pyrrdorm.add(ProcDiskstatsTable)
    pyrrdorm.add(ProcBatTable)

    pyrrdorm.run("./system_data")
